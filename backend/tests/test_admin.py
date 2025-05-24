# ===========================================================================================
# Django Admin Tests for Table Model
# ===========================================================================================
# This module contains test cases for verifying the registration and functionality of the 
# Table model in the Django Admin interface.
#
# Tested Features:
# - Ensures the Table model is registered in Django Admin.
# - Verifies admin panel settings such as list display fields.
# - Confirms superuser access to the Django Admin UI.
# - Tests Admin search and filter functionalities.
#
# Author: Daria Ilchenko
# Date: 02/25/2025
# ===========================================================================================

from django.contrib.admin.sites import site
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Table  # Import Table model
from core.admin import TableAdmin  # Import TableAdmin class


class TableAdminTest(TestCase):
    # Test suite for Table model registration and accessibility in Django Admin.

    @classmethod
    def setUpTestData(cls):
        # Set up initial data for testing.
        #
        # - Creates a Table instance for testing.
        # - Creates a superuser to access the Django Admin panel.
        
        cls.table = Table.objects.create(
            table_id=1,  # Explicitly setting primary key to ensure consistent test data
            table_name="Test Table",
            description="Test description",
            use_cases="Test use cases",
            important_notes="Test notes"
        )

        # Create a superuser to test Django Admin login and access
        cls.superuser = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

    def test_table_registered_in_admin(self):
        # Test if the Table model is registered in the Django Admin interface.
        #
        # - Retrieves all registered models from `site._registry`.
        # - Ensures the Table model is present in the registry.
        
        self.assertIn(Table, site._registry)  # Ensures Table model is registered

    def test_table_admin_list_display(self):
        # Test the list_display settings for the Table model in Django Admin.
        #
        # - Checks if the TableAdmin class defines the correct fields for display.
        # - Ensures consistency with expected admin configurations.

        admin_instance = TableAdmin(Table, site)  # Use Table model class, not instance
        self.assertEqual(
            admin_instance.list_display,
            ("table_id", "table_name", "description", "use_cases", "important_notes")
        )

    def test_admin_can_access_tables(self):
        # Test if an admin user can log in and access the Table model in Django Admin.
        #
        # - Logs in with the superuser created in setUpTestData.
        # - Sends a GET request to the Table model’s Django Admin page.
        # - Verifies that the page loads successfully with status code 200.
        
        login = self.client.login(username="admin", password="testpassword")
        self.assertTrue(login)  # Confirms that superuser login was successful

        # Dynamically generate the admin URL based on the app label and model name
        response = self.client.get(f"/admin/{Table._meta.app_label}/{Table._meta.model_name}/")
        self.assertEqual(response.status_code, 200)  # Ensures Admin UI is accessible

    def test_admin_search_functionality(self):
        # Test if the Table model search functionality works in Django Admin.
        #
        # - Retrieves the search fields defined in TableAdmin.
        # - Ensures `table_id` and `table_name` are included in search fields.

        admin_instance = TableAdmin(Table, site)
        search_fields = admin_instance.get_search_fields(request=None)

        self.assertIn("table_id", search_fields)
        self.assertIn("table_name", search_fields)

    def test_admin_list_filter(self):
        # Ensures filtering in Django Admin is set up correctly.
        #
        # - Checks if "description" appears in list_filter settings.

        admin_instance = TableAdmin(Table, site)
        filter_fields = admin_instance.get_list_filter(request=None)

        self.assertIn("description", filter_fields)
        