"""
urls.py

This module defines all URL routes for the 'core' app in the L@S Data Dictionary project.
It includes both router-registered viewsets and custom API endpoints.

Registered ViewSets:
- TableNameViewSet: CRUD operations for TableName model.
- FieldViewSet, LabelViewSet, EntryViewSet, CategoryViewSet: Manage related models.

Custom Endpoints:
- /tooltips/: Returns a list of UI tooltips.
- /tables/: Retrieves tables along with their fields.
- /search/: Performs text-based table search.
- /friendly-name-search/: Searches entries using friendly names.
- /friendly-name-autofill/: Provides autofill suggestions for friendly names.
- /api/health/: Returns server status for health monitoring.

These routes are consumed by the frontend to access and manipulate model data via RESTful APIs.
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TableWithFieldsView
from .views import FieldViewSet
from .views import TableSearchAPIView
from .views import LabelViewSet
from .views import EntryViewSet
from .views import friendly_name_search
from .views import CategoryViewSet
from .views import friendly_name_autofill


# Router and register
router = DefaultRouter()
router.register(r'fields', FieldViewSet, basename='fields')
router.register(r'labels', LabelViewSet, basename='labels')
router.register(r'entries', EntryViewSet, basename='entries')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    # Include DRF-generated URLs for ViewSet
    path('', include(router.urls)),

    # Existing endpoints
    path('api/health/', views.health_check, name='health-check'),
    path('tables/', TableWithFieldsView.as_view(), name='table-list'),
    path('search/', TableSearchAPIView.as_view(), name='table-search'),
    path('friendly-name-search/', friendly_name_search, name='friendly-name-search'),
    path('friendly-name-autofill/', views.friendly_name_autofill),
]
