"""
serializers.py

This module defines serializers for the 'core' app models in the L@S Data Dictionary project.
Serializers translate model instances into JSON for API responses and handle input validation for incoming data.

Included Serializers:
- CategorySerializer: Serializes all fields from the Category model.
- EntrySerializer: Serializes all fields from the Entry model.
- LabelSerializer: Serializes all fields from the Label model.
- FieldSerializer: Serializes selected fields from the Field model.
- TableSerializer: Serializes Table model fields and includes nested Field objects, ordered by position.
- TableNameSerializer: Handles all fields of TableName with custom validation logic for name and description.

These serializers are used by views and API endpoints to enforce clean data handling and structured output.
"""


from rest_framework import serializers
from .models import Table, Field, Label, Entry, Category

#Serializer for category objects
class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'

#Serilaizer for entry objects
class EntrySerializer(serializers.ModelSerializer):
   class Meta:
      model = Entry
      fields = '__all__'

# Serializer for Label Objects
class LabelSerializer(serializers.ModelSerializer):
   class Meta:
      model = Label
      fields = '__all__'

# Serializer for Field objects
class FieldSerializer(serializers.ModelSerializer):
  class Meta:
    model = Field
    fields = ['field_id', 'field_name', 'description', 'position']

# Serializer for Table objects, including related fields
class TableSerializer(serializers.ModelSerializer):
  # Fetch related fields
  fields = FieldSerializer(many=True, read_only=True)
  class Meta:
    model = Table
    fields = ['table_id', 'table_name', 'description', 'use_cases', 'important_notes', 'fields']

  # Ensuring fields are sorted by position before sending the response
  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['fields'] = sorted(representation['fields'], key=lambda x: x['position'])
    return representation
