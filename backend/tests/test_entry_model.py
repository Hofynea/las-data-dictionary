# ===========================================================================================
# Tests for Entry Model
# ===========================================================================================
# This module contains test cases for verifying the creation and functionality of the Entry model based on the ERD.
#
# Tested Features:
# - Verified creation of an Entry instance with valid Foreign Keys.
# - Verified that an Entry cannot be created without entry_content.
# - Verified that Entry is properly linked to a Field.
# - Verified that Entry is properly linked to a Label.
# - Verified that deleting a Field deletes associated Entries (CASCADE DELETE).
# - Verified that deleting a Label deletes associated Entries (CASCADE DELETE).
# - Confirmed that __str__ returns the correct representation of Entry instance.
#
# Author: Zulfina Ivanova
# Date: 03/04/2025
# ===========================================================================================

import pytest
from django.core.exceptions import ValidationError
from core.models import Entry, Field, Label, Table

"""Testing creation of an Entry instance with valid Foreign Keys."""
@pytest.mark.django_db
def test_create_entry():
  # Creating a Table instance
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  # Creating a field instance
  field = Field.objects.create(
    field_name="Test Field",
    description="A sample field",
    position=1
  )

  # Creating a label instance
  label = Label.objects.create(
    label_name="Test Label",
    label_index=1,
    table_id=table
  )

  # Finally creating entry instance
  entry = Entry.objects.create(
    entry_content="This is a test entry",
    field=field,
    label=label
  )

  assert entry.entry_id is not None
  assert entry.entry_content == "This is a test entry"
  assert entry.field == field
  assert entry.label == label


"""Testing that an Entry cannot be created without entry_content."""
@pytest.mark.django_db
def test_entry_missing_content():
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  field = Field.objects.create(
    field_name="Test Field",
    description="A sample field",
    position=1
  )

  label = Label.objects.create(
    label_name="Test Label",
    label_index=1,
    table_id=table
  )

  entry = Entry(
    entry_content="",  # Empty content
    field=field,
    label=label
  )

  with pytest.raises(ValidationError):
    entry.full_clean()
    entry.save()



"""Testing that Entry is properly linked to a Field."""
@pytest.mark.django_db
def test_entry_field_relationship():
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  field = Field.objects.create(
    field_name="Linked Field",
    description="A linked test field",
    position=1
  )

  label = Label.objects.create(
    label_name="Label 1",
    label_index=1,
    table_id=table
  )

  entry = Entry.objects.create(
    entry_content="Entry linked to field",
    field=field,
    label=label
  )

  assert entry.field.field_name == "Linked Field"



"""Testing that Entry is properly linked to a Label."""
@pytest.mark.django_db
def test_entry_label_relationship():
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  field = Field.objects.create(
    field_name="Field for Label Test",
    description="A field for testing label relationship",
    position=1
  )
  label = Label.objects.create(
    label_name="Test Label Relationship",
    label_index=1,
    table_id=table
  )

  entry = Entry.objects.create(
    entry_content="Testing label relation",
    field=field,
    label=label
  )

  assert entry.label.label_name == "Test Label Relationship"


"""Testing that deleting a Field deletes associated Entries (CASCADE DELETE)."""
@pytest.mark.django_db
def test_cascade_delete_entry_on_field_deletion():
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  field = Field.objects.create(
    field_name="Field to be deleted",
    description="A field that will be deleted",
    position=1
  )

  label = Label.objects.create(
    label_name="Label for deletion test",
    label_index=1,
    table_id=table
  )

  entry = Entry.objects.create(
    entry_content="Entry should be deleted when field is deleted",
    field=field,
    label=label
  )

  field.delete()  # Deleting field

  assert Entry.objects.filter(entry_id=entry.entry_id).count() == 0



"""Testing that deleting a Label deletes associated Entries (CASCADE DELETE)."""
@pytest.mark.django_db
def test_cascade_delete_entry_on_label_deletion():
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  field = Field.objects.create(
    field_name="Field remains",
    description="A field that will not be deleted",
    position=1
  )

  label = Label.objects.create(
    label_name="Label to be deleted",
    label_index=1,
    table_id=table
  )

  entry = Entry.objects.create(
    entry_content="Entry should be deleted when label is deleted",
    field=field,
    label=label
  )

  label.delete()  # Deleting label

  assert Entry.objects.filter(entry_id=entry.entry_id).count() == 0


"""Testing the __str__ representation of Entry"""
@pytest.mark.django_db
def test_entry_str_representation():
  table = Table.objects.create(
    table_id=1,
    table_name="Test Table"
  )

  field = Field.objects.create(
    field_name="Sample Field",
    description="A test field",
    position=2
  )

  label = Label.objects.create(
    label_name="Sample Label",
    label_index=2,
    table_id=table
  )

  entry = Entry.objects.create(
    entry_content="Sample Entry Content",
    field=field,
    label=label
  )

  assert str(entry) == "Sample Entry Content"
