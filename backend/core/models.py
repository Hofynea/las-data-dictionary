"""
models.py

This module defines all database models for the 'core' app in the L@S Data Dictionary project.
These models represent the core structure for educational data representation and metadata mapping.

Main Models:
- Table: Represents a database-style table with metadata like description and use cases.
- Field: Describes individual columns/fields within tables, including name, description, and position.
- Category: Groups labels into meaningful categories to support organized labeling.
- Label: Identifies labeled markers within the data dictionary, linked to specific tables and categories.
- Entry: Connects field data to labels, representing values shown to users.
- Tooltips (Outdated): Legacy model for displaying contextual tooltips in the UI.
- TableName (Outdated): Earlier schema for managing table metadata with timestamp tracking.

Each model includes verbose names and admin ordering, with relationships clearly defined via ForeignKey and ManyToMany fields.
"""

from django.db import models

# Create your models here.

class Table (models.Model): #table entity
  table_id=models.IntegerField ( #Primary Key
    unique=True,
    primary_key=True
  )


  table_name = models.CharField(
    max_length=30,
    blank=False,
    unique=True
  )

  description = models.TextField(
    blank=False
  )

  use_cases = models.TextField(
    blank=False
  )

  important_notes = models.TextField(
    blank=False
  )

  class Meta:
    verbose_name = 'Table'
    verbose_name_plural = 'Tables'
    ordering = ['table_name']

  def __str__(self):
    return self.table_name


# Field entity model
class Field(models.Model):
  # Primary key
  field_id = models.AutoField (
       unique=True,
       primary_key=True
  )

  # Field name
  field_name = models.CharField(
    max_length=100,
    blank=False,
    help_text='Enter the name of the field'
  )

  # Field description
  description = models.TextField(
    blank=False,
    help_text='Provide a description of the field'
  )

  # Field position
  position = models.PositiveIntegerField(
    blank=False,
    help_text='Position of the field in the table'
  )

  # Many-to-Many relationship with Table
  tables = models.ManyToManyField(
    Table,
    related_name='fields',  # Allows reverse access from Table
    blank=True
  )

  class Meta:
    verbose_name = 'Field'
    verbose_name_plural = 'Fields'
    ordering = ['field_name']

  def __str__(self):
    return self.field_name


# Category Model
class Category(models.Model):
  # Primary Key
  category_id = models.AutoField(primary_key=True)
  # Name of the category
  category_name = models.CharField(
    max_length=255,
    unique = True,
    db_index=True,
    help_text = 'Enter a category name',
    null = True
  )

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    ordering = ['category_name']

  def __str__(self):
    return self.category_name



#label model
class Label(models.Model):
  #Primary Key
  label_id=models.AutoField(
    unique=True,
    primary_key=True
  )

  label_name=models.CharField(
    max_length=100,
    blank=False,
    help_text='Enter the name of the label'
  )

  label_index=models.PositiveBigIntegerField(
    blank=False,
    help_text='Index of the label in the table'
  )

  #Foreign Key Relationship with Table
  table_id=models.ForeignKey(
    Table,
    on_delete=models.CASCADE)

  # Foreign Key Relationship with Category
  category = models.ForeignKey(
    Category,
    null=True,
    blank=True,
    on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Label'
    verbose_name_plural = 'Labels'
    ordering = ['label_name']

  def __str__(self):
    return self.label_name



# Entry entity model
class Entry(models.Model):
  # Primary Key
  entry_id = models.AutoField(
    primary_key=True,
    unique=True
  )

  # Entry content
  entry_content = models.TextField(
    blank=False,
    help_text="Content of the entry"
  )

  # Foreign Key Relationship with Field
  field = models.ForeignKey(
    Field,
    on_delete=models.CASCADE,
    related_name="entries",
    help_text="The field associated with this entry"
  )

  # Foreign Key Relationship with Label
  label = models.ForeignKey(
    Label,
    on_delete=models.CASCADE,
    related_name="entries",
    help_text="The label associated with this entry"
  )

  class Meta:
    verbose_name = "Entry"
    verbose_name_plural = "Entries"
    ordering = ['entry_id']

  def __str__(self):
    return f"{self.entry_content}"







