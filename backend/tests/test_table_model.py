# ===========================================================================================
# Tests for Table Model
# ===========================================================================================
# This module contains test cases for verifying the creation and functionality of the Table model based on the ERD.
#
# Tested Features:
# - Verified proper creation of a Table model instance.
# - Verified that table_name must be unique.
# - Ensured that missing required fields trigger an error.
# - Confirmed that __str__ returns the correct table name.
#
# Author: Zulfina Ivanova
# Date: 03/03/2025
# ===========================================================================================

import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from core.models import Table


"""  the creation of a Table instance."""
@pytest.mark.django_db
def test_create_table():

  # Creating a Table instance"""
  table = Table.objects.create(
    table_id=1,
    table_name="Student Class",
    description="Student Class table description.",
    important_notes="Student Class table notes.",
    use_cases="Student Class table use cases."
  )

  # Fetching newly created table instance from DB to confirm
  saved_table = Table.objects.get(table_id=1)

  assert saved_table.table_name == "Student Class"
  assert saved_table.description == "Student Class table description."
  assert saved_table.use_cases == "Student Class table use cases."
  assert saved_table.important_notes == "Student Class table notes."


"""Testing that creating a table with a duplicate name raises an error."""
@pytest.mark.django_db
def test_unique_table_name():
  # Creating a Table instance"""
  Table.objects.create(
    table_id=1,
    table_name="Student Class",
    description="Student Class table description.",
    use_cases="Student Class table use cases.",
    important_notes="Granularity: One row per student and class."
  )

  # Testing creation of a table instance with duplicate table_name
  with pytest.raises(IntegrityError):
    Table.objects.create(
      table_id=2,
      table_name="Student Class",
      description="Another Student Class table description.",
      use_cases="Another Student Class table use cases.",
      important_notes="Student Class table notes."
    )

"""Testing that missing required fields raises an error."""
@pytest.mark.django_db
def test_missing_required_fields():
  # Testing creation of a table instance with missing required field

  table = Table(
    table_id=3,
    # Empty string for table_name
    table_name=""
  )

  with pytest.raises(ValidationError):
    table.full_clean()
    table.save()

"""Testing the __str__ method of the Table model."""
@pytest.mark.django_db
def test_table_str():

    table = Table.objects.create(
        table_id=4,
        table_name="Class Term",
        description="Class Term table description.",
        use_cases="Class Term table use cases.",
        important_notes="Class Term table notes."
    )

    assert str(table) == "Class Term"


