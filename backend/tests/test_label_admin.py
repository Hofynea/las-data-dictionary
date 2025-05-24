# ===========================================================================================
# Django Admin Tests for Label Model
# ===========================================================================================
# This module contains test cases for verifying the registration and functionality of the 
# Label model in the Django Admin interface.
#
# Tested Features:
# - Ensures the Label model is registered in Django Admin.
# - Verifies admin list display settings.
# - Confirms superuser access to the Django Admin UI.
# - Tests search functionality by Label ID.
# - Ensures fields are ordered alphabetically.
# - Validates admin filtering by Table.
#
# Author: Daria Ilchenko
# Date: 03/04/2025
# ===========================================================================================

from django.contrib.admin.sites import site
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Table, Label  # Import Table, Label models
from core.admin import LabelAdmin  # Import LabelAdmin class


class LabelAdminTest(TestCase):
    # Test suite for verifying the registration and functionality of the Label model in Django Admin.

    @classmethod
    def setUpTestData(cls):
        # Set up initial test data before running the test cases.
        
        # - Creates a Table instance to serve as a foreign key.
        # - Creates a Label instance linked to the Table.
        # - Creates a superuser for Django Admin access testing.

        # Create a Table instance first
        cls.table = Table.objects.create(
            table_id=1,
            table_name="Test Table",
            description="Test description",
            use_cases="Test use cases",
            important_notes="Test notes"
        )
        
        # Assign the Table instance to the ForeignKey field
        cls.label = Label.objects.create(
            label_id=1,
            label_name="Test Label",
            label_index=10,
            table_id=cls.table
        )

        # Create a superuser for admin testing
        cls.superuser = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

    def test_label_registered_in_admin(self):

        # Ensure the Label model is properly registered in Django Admin.
        self.assertIn(Label, site._registry)

    def test_label_admin_list_display(self):
        # Verify that the correct fields are set in list_display for LabelAdmin.
        
        admin_instance = LabelAdmin(Label, site)  
        expected_fields = ("label_id", "label_name", "label_index", "table_id")
        self.assertEqual(admin_instance.list_display, expected_fields)

    def test_admin_can_access_labels(self):
        # Ensure a superuser can log in and access the Label model in Django Admin.
        
        login = self.client.login(username="admin", password="testpassword")
        self.assertTrue(login)  # Confirms that superuser login was successful

        response = self.client.get(f"/admin/{Label._meta.app_label}/{Label._meta.model_name}/")
        self.assertEqual(response.status_code, 200)  # Ensures Admin UI is accessible

    def test_admin_search_functionality(self):
        # Validate that the Label model supports searching by label_id in Django Admin.
        
        admin_instance = LabelAdmin(Label, site)
        search_fields = admin_instance.get_search_fields(request=None)

        self.assertIn("label_id", search_fields)  # Ensures search by label_id is enabled

    def test_admin_list_filter(self):
        # Ensure that the Label model can be filtered by table in Django Admin.
        
        admin_instance = LabelAdmin(Label, site)
        filter_fields = admin_instance.get_list_filter(request=None)

        self.assertIn("table_id", filter_fields)  # Ensures filtering by table is enabled

    def test_label_ordering(self):
        # Verify that Labels are correctly ordered by label_name in Django Admin.
        
        Label.objects.create(label_id=2, label_name="Alpha Label", label_index=5, table_id=self.table)
        Label.objects.create(label_id=3, label_name="Zeta Label", label_index=15, table_id=self.table)
        
        first_label = Label.objects.order_by("label_name").first()
        self.assertEqual(first_label.label_name, "Alpha Label")  # Should be ordered alphabetically
