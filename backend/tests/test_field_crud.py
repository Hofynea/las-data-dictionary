# ===========================================================================================
# CRUD Unit Tests for Field Model via Django ORM
# ===========================================================================================
# This module contains unit test cases that verify the ability of an admin user to perform
# CRUD (Create, Read, Update, Delete) operations on the Field model.
#
# Tested Features:
# - Admin can create a new Field
# - Admin can retrieve an existing Field
# - Admin can update a Field
# - Admin can delete a Field
#
# Author: Daria Ilchenko
# Date: 04/23/2025
# ===========================================================================================

from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Field

class FieldCRUDTest(TestCase):
    # Test suite for admin-level CRUD operations on the Field model.

    @classmethod
    def setUpTestData(cls):
        # Set up initial data and superuser.
        cls.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

        cls.initial_field = Field.objects.create(
            field_id=1,
            field_name="Initial Field",
            description="Initial description",
            position=1
        )

    def test_create_field(self):
        # Verifies that a Field can be created successfully using ORM.
        field = Field.objects.create(
            field_id=2,
            field_name="Created Field",
            description="Created description",
            position=2
        )
        self.assertEqual(field.field_name, "Created Field")
        self.assertTrue(Field.objects.filter(field_name="Created Field").exists())

    def test_read_field(self):
        # Verifies that an existing Field can be retrieved.
        field = Field.objects.get(field_id=1)
        self.assertEqual(field.field_name, "Initial Field")

    def test_update_field(self):
        # Verifies that a Field can be updated using ORM.
        field = Field.objects.get(field_id=1)
        field.field_name = "Updated Field"
        field.save()

        updated = Field.objects.get(field_id=1)
        self.assertEqual(updated.field_name, "Updated Field")

    def test_delete_field(self):
        # Verifies that a Field can be deleted and is no longer in the database.
        field = Field.objects.create(
            field_id=3,
            field_name="Temp Field",
            description="To be deleted",
            position=3
        )
        field.delete()
        self.assertFalse(Field.objects.filter(field_id=3).exists())
