# ===========================================================================================
# Tests for Field Model
# ===========================================================================================
# This module contains test cases for verifying the creation and functionality of the field model based on the ERD.
#
# Tested Features:
# - Verified proper creation of a field model instance.
# - Ensured that missing required fields trigger an error.
#
# Author: Seth Cabral
# Date: 03/07/2025
# ===========================================================================================

import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from core.models import Field

""" Creation of a field instance"""
@pytest.mark.django_db
def test_create_field():
    field = Field.objects.create(
        field_id = 2,
        field_name = "Friendly Name",
        description = "A nontechnical name used to more easily describe and identify the data element for the data dictionary",
        position = 2
    )

    #Grab created instance
    saved_field = Field.objects.get(field_id = 2)

    assert saved_field.field_name == "Friendly Name"
    assert saved_field.description == "A nontechnical name used to more easily describe and identify the data element for the data dictionary"
    assert saved_field.position == 2

""" Test Missing Field """
@pytest.mark.django_db
def test_missing_required_fields():
    field = Field (
        field_id = 3 ,
        # Empty string
        field_name=""
    )
    with pytest.raises(ValidationError):
        field.full_clean()
        field.save()


