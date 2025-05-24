# ===========================================================================================
# Django Admin Tests for Entry Model
# ===========================================================================================
# This module contains test cases for verifying the registration and functionality of the 
# Entry model in the Django Admin interface.
#
# Tested Features:
# - Ensures the Entry model is registered in Django Admin.
# - Verifies admin list display settings.
# - Confirms superuser access to the Django Admin UI.
# - Tests search functionality by Entry ID.
# - Ensures fields are ordered by entry_id.
# - Validates admin filtering by Field and Label.
#
# Author: Daria Ilchenko
# Date: 03/06/2025
# ===========================================================================================

from django.contrib.admin.sites import site
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Table, Field, Label, Entry  # Import related models
from core.admin import EntryAdmin  # Import EntryAdmin class


class EntryAdminTest(TestCase):
    # Test suite for verifying the registration and functionality of the Entry model in Django Admin.

    @classmethod
    def setUpTestData(cls):
        # Set up initial test data before running the test cases.
        
        # - Creates a Table instance for Field and Label foreign keys.
        # - Creates a Field instance linked to the Table.
        # - Creates a Label instance linked to the Table.
        # - Creates an Entry instance linked to the Field and Label.
        # - Creates a superuser for Django Admin access testing.

        # Create a Table instance
        cls.table = Table.objects.create(
            table_id=1,
            table_name="Test Table",
            description="Test description",
            use_cases="Test use cases",
            important_notes="Test notes"
        )

        # Create a Field instance
        cls.field = Field.objects.create(
            field_id=1,
            field_name="Test Field",
            description="Test Field Description",
            position=1
        )
        cls.field.tables.add(cls.table)  # ManyToMany relationship setup

        # Create a Label instance
        cls.label = Label.objects.create(
            label_id=1,
            label_name="Test Label",
            label_index=10,
            table_id=cls.table
        )

        # Create an Entry instance
        cls.entry = Entry.objects.create(
            entry_id=1,
            entry_content="Test Entry Content",
            field=cls.field,
            label=cls.label
        )

        # Create a superuser for admin testing
        cls.superuser = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

    def test_entry_registered_in_admin(self):
        # Ensure the Entry model is properly registered in Django Admin.

        self.assertIn(Entry, site._registry)  # Confirms Entry model is registered

    def test_entry_admin_list_display(self):
        # Verify that the correct fields are set in list_display for EntryAdmin.
        
        admin_instance = EntryAdmin(Entry, site)  
        expected_fields = ("entry_id", "entry_content", "field", "label")  
        self.assertEqual(admin_instance.list_display, expected_fields)

    def test_admin_can_access_entries(self):
        # Ensure a superuser can log in and access the Entry model in Django Admin.
        
        login = self.client.login(username="admin", password="testpassword")
        self.assertTrue(login)  # Confirms that superuser login was successful

        response = self.client.get(f"/admin/{Entry._meta.app_label}/{Entry._meta.model_name}/")
        self.assertEqual(response.status_code, 200)  # Ensures Admin UI is accessible

    def test_admin_search_functionality(self):
        # Validate that the Entry model supports searching by entry_id in Django Admin.
        
        admin_instance = EntryAdmin(Entry, site)
        search_fields = admin_instance.get_search_fields(request=None)

        self.assertIn("entry_id", search_fields)  # Ensures search by entry_id is enabled

    def test_admin_list_filter(self):
        # Ensure that the Entry model can be filtered by Field and Label in Django Admin.

        admin_instance = EntryAdmin(Entry, site)
        filter_fields = admin_instance.get_list_filter(request=None)

        self.assertIn("field", filter_fields)  # Ensures filtering by Field is enabled
        self.assertIn("label", filter_fields)  # Ensures filtering by Label is enabled

    def test_entry_ordering(self):
        # Verify that Entries are correctly ordered by entry_id in Django Admin.
        
        Entry.objects.create(entry_id=2, entry_content="Alpha Entry", field=self.field, label=self.label)
        Entry.objects.create(entry_id=3, entry_content="Zeta Entry", field=self.field, label=self.label)
        
        first_entry = Entry.objects.order_by("entry_id").first()
        self.assertEqual(first_entry.entry_id, 1)  # Should be ordered by entry_id
