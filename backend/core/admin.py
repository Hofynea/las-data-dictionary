"""
admin.py

This module registers all custom models to the Django admin site for the L@S Data Dictionary application.
It defines how each model should be displayed, searched, and organized in the admin interface.

Models registered:
- Tooltips: Tooltip labels and descriptions for UI guidance.
- TableName: Represents named tables with timestamp metadata.
- Table: Defines detailed data tables with use cases and notes.
- Field: Represents individual fields within tables.
- Category: Categorizes data types for better structure.
- Label: Positional labels for UI arrows/indicators.
- Entry: Holds user-facing values for each field-label combination.

Each admin class customizes list display, filtering, searching, and ordering for improved usability.
"""

from django.contrib import admin
from .models import Table, Field # Import Table and Field models
from .models import Category, Label, Entry # Import Category, Label, Entry models


# Register Table in Admin with basic configurations
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_id", "table_name", "description", "use_cases", "important_notes")
    search_fields = ("table_id", "table_name")
    list_filter = ("description",)
    ordering = ("table_name",)

# Register Field in Admin with basic configurations
@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ("field_id", "field_name", "description", "position")
    search_fields = ("field_id", "field_name")
    list_filter = ("position",)
    ordering = ("field_name",)

# Register Category in Admin with basic configurations
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_name")
    search_fields = ("category_id",)
    ordering = ("category_name",)

# Register Label in Admin with basic configurations
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("label_id", "label_name", "label_index", "table_id")
    search_fields = ("label_id",)
    list_filter = ("table_id",)
    ordering = ("label_name",)

# Register Entry in Admin with basic configurations
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("entry_id", "entry_content", "field", "label")
    search_fields = ("entry_id",)
    list_filter = ("field", "label")
    ordering = ("entry_id",)
