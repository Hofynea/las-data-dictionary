"""
views.py

This module defines all API views and viewsets for the 'core' app in the L@S Data Dictionary project.
It includes both class-based and function-based views to handle CRUD operations and custom search endpoints.

Main Components:
- ViewSets: TableNameViewSet, FieldViewSet, LabelViewSet, EntryViewSet, CategoryViewSet
- List & Detail Views: TableWithFieldsView, TooltipListView, TableNamesView
- Custom APIs: health_check, TableSearchAPIView, friendly_name_search, friendly_name_autofill

These views support full RESTful interaction with backend models and are consumed by the frontend application.
"""


from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView # Added APIView for converting function-based views
from rest_framework.permissions import AllowAny # Added AllowAny permission to aloow unrestricted access where needed
from rest_framework import status, viewsets # Added viewsets for better API management
import json
from .models import Table, Field, Label, Entry, Category #Models for database
from .serializers import TableSerializer, FieldSerializer, LabelSerializer, EntrySerializer, CategorySerializer # Serializers
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination # Pagination class for handling large datasets
from django.db.models import Prefetch # Used for optimizing related field lookups in querysets
from core.models import Label, Entry, Field, Table

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self):
        queryset = Entry.objects.all().order_by('field_id')

        label_id = self.request.query_params.get('label_id')
        field_id = self.request.query_params.get('field_id')

        if label_id:
            queryset = queryset.filter(label_id=label_id)

        if field_id:
            queryset = queryset.filter(field_id=field_id)

        return queryset

class LabelViewSet(viewsets.ModelViewSet):
    serializer_class = LabelSerializer

    def get_queryset(self):
        queryset = Label.objects.all().order_by('label_index')
        table_id = self.request.query_params.get('table_id')

        if table_id:  # Check if `table_id` was provided
            try:
                table_id = int(table_id)  # Convert to integer
                queryset = queryset.filter(table_id=table_id)
            except ValueError:
                pass

        return queryset

# API Generic View for fields that will be dynamically queried
class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all().order_by('position')
    serializer_class = FieldSerializer

# API View that returns all tables with their related fields
class TableWithFieldsView(generics.ListAPIView):
  serializer_class = TableSerializer

  def get_queryset(self):
        queryset = Table.objects.prefetch_related('fields').order_by('table_id').distinct()

        table_name = self.request.query_params.get('table_name', '').strip()
        category = self.request.query_params.get('category', '').strip()

        if table_name:
            queryset = queryset.filter(table_name__icontains=table_name)

        if category:
            queryset = Table.objects.filter(
                label__category__category_name__icontains=category
            ).distinct()

        return queryset

  pagination_class = PageNumberPagination

# Health Check Endpoint
def health_check(request):
    return JsonResponse({"status": "Backend is running!"})


class TableSearchAPIView(APIView):
  """
  API endpoint to handle table searches.
  Searches through the table name, description, and use cases.
  """

  def get(self, request, format=None):
    search_query = request.GET.get('query', '')

    if not search_query:
      return Response({"error": "No search term provided"}, status=status.HTTP_400_BAD_REQUEST)

    results = Table.objects.filter(
      Q(table_name__icontains=search_query) |
      Q(description__icontains=search_query) |
      Q(use_cases__icontains=search_query)
    )

    serializer = TableSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def friendly_name_search(request):
    query = request.GET.get('query', '').lower()

    if not query:
        return Response({"error": "No search term provided"}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch entries where the entry_content matches the query
    entries = Entry.objects.select_related('label__table_id').filter(
        Q(entry_content__icontains=query) |
        Q(label__label_name__icontains=query)
    ).order_by('label__label_index', 'field_id')  # Keep natural ordering

    # Group entries by label
    label_to_entries = {}
    for entry in entries:
        label_id = entry.label.label_id
        if label_id not in label_to_entries:
            label_to_entries[label_id] = {
                "label": entry.label.label_name,
                "table_name": entry.label.table_id.table_name if entry.label.table_id else "N/A",
                "entries": []
            }
        label_to_entries[label_id]["entries"].append(entry.entry_content)

    # Build results
    results = []
    for label_data in label_to_entries.values():
        entries_list = label_data["entries"]

        row = {
            "label": label_data["label"],
            "friendly_name": entries_list[0] if len(entries_list) > 0 else "N/A",
            "description": entries_list[1] if len(entries_list) > 1 else "N/A",
            "category": entries_list[2] if len(entries_list) > 2 else "N/A",
            "source": entries_list[3] if len(entries_list) > 3 else "N/A",
            "name": entries_list[4] if len(entries_list) > 4 else "N/A",
            "dataset_name": entries_list[5] if len(entries_list) > 5 else "N/A",
            "sample_data": entries_list[6] if len(entries_list) > 6 else "N/A",
            "deidentified": entries_list[7] if len(entries_list) > 7 else "N/A",
            "additional_notes": entries_list[8] if len(entries_list) > 8 else "N/A",
            "data_type": entries_list[9] if len(entries_list) > 9 else "N/A",
            "table_name": label_data["table_name"]
        }
        results.append(row)

    return Response(results, status=status.HTTP_200_OK)

@api_view(['GET'])
def friendly_name_autofill(request):
    query = request.GET.get('query', '').lower()
    labels = Label.objects.all()
    suggestions = []

    for label in labels:
        entries = Entry.objects.filter(label=label).order_by('entry_id')
        if entries.exists():
            friendly_name = entries[0].entry_content
            if query in friendly_name.lower():
                suggestions.append(friendly_name)

    suggestions = list(set(suggestions))[:10]
    return Response(suggestions)
