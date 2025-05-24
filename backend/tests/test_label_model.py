# ===========================================================================================
# Tests for Label Model
# ===========================================================================================
# This module contains test cases for verifying the creation and functionality of the label model based on the ERD.
#
# Tested Features:
# - Ensured that missing required label trigger an error.
#
# Author: Seth Cabral
# Date: 03/07/2025
# ===========================================================================================

import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from core.models import Label

""" Test Missing Field """
@pytest.mark.django_db
def test_missing_required_fields():
    label = Label (
        label_id = 3 ,
        # Empty string
        label_name=""
    )
    with pytest.raises(ValidationError):
        label.full_clean()
        label.save()