# ===========================================================================================
# Tests for Category Model
# ===========================================================================================
# This module contains test cases for verifying the creation and functionality of the Category model based on the ERD.
#
# Tested Features:
# - Verified proper creation of a Category model instance.
# - Verified that category_name must be unique.
# - Ensured that missing required fields trigger an error.
# - Confirmed that __str__ returns the correct category name.
#
# Author: Zulfina Ivanova
# Date: 03/04/2025
# ===========================================================================================

import pytest
from django.core.exceptions import ValidationError
from core.models import Category

"""Testing creation of a Category instance."""
@pytest.mark.django_db
def test_create_category():
  category = Category.objects.create(
    category_name="Academic"
  )

  assert category.category_id is not None
  assert category.category_name == "Academic"

"""Testing that creating a duplicate category raises an error."""
@pytest.mark.django_db
def test_category_name_unique():
  Category.objects.create(category_name="Academic")

  with pytest.raises(Exception):
    Category.objects.create(category_name="Academic")


"""Testing that missing required fields raises an error."""
@pytest.mark.django_db
def test_category_missing_name():
  category = Category(category_name="")  # Empty name

  with pytest.raises(ValidationError):
    category.full_clean()
    category.save()

"""Testing the __str__ method of the Category model."""
@pytest.mark.django_db
def test_table_str():
  category = Category.objects.create(
    category_name="Academic"
  )
  assert str(category) == "Academic"
