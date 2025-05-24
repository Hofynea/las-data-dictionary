# ===========================================================================================
# CRUD Unit Tests for Label Model via Django ORM
# ===========================================================================================
# This module contains unit test cases that verify the ability of an admin user to perform
# CRUD (Create, Read, Update, Delete) operations on the Label model.
#
# Tested Features:
# - Admin can create a new Label
# - Admin can retrieve an existing Label
# - Admin can update a Label
# - Admin can delete a Label
#
# Author: Daria Ilchenko
# Date: 04/21/2025
# ===========================================================================================

from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Label, Table


class LabelCRUDTest(TestCase):
    # Test suite for admin-level CRUD operations on the Label model.

    @classmethod
    def setUpTestData(cls):
        # Set up initial data and superuser.
        cls.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

        # Create a test table to associate labels with
        cls.test_table = Table.objects.create(
            table_id=1,
            table_name="Test Table",
            description="Test",
            use_cases="Use cases",
            important_notes="Some notes"
        )

        cls.initial_label = Label.objects.create(
            label_id=1,
            label_name="Initial Label",
            label_index=1,
            table_id=cls.test_table
        )

    def test_create_label(self):
        # Verifies that a Label can be created successfully using ORM.
        label = Label.objects.create(
            label_id=2,
            label_name="Created Label",
            label_index=2,
            table_id=self.test_table
        )

        self.assertEqual(label.label_name, "Created Label")
        self.assertTrue(Label.objects.filter(label_name="Created Label").exists())

    def test_read_label(self):
        # Verifies that an existing Label can be retrieved.
        label = Label.objects.get(label_id=1)
        self.assertEqual(label.label_name, "Initial Label")

    def test_update_label(self):
        # Verifies that a Label can be updated using ORM.
        label = Label.objects.get(label_id=1)
        label.label_name = "Updated Label"
        label.save()

        updated = Label.objects.get(label_id=1)
        self.assertEqual(updated.label_name, "Updated Label")

    def test_delete_label(self):
        # Verifies that a Label can be deleted and is no longer in the database.
        label = Label.objects.create(
            label_id=3,
            label_name="Temp Label",
            label_index=3,
            table_id=self.test_table
        )
        label.delete()
        self.assertFalse(Label.objects.filter(label_id=3).exists())
        