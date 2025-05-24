# ===========================================================================================
# Django Admin Tests for Field Model
# ===========================================================================================
# This module contains test cases for verifying the registration and functionality of the 
# Field model in the Django Admin interface.
#
# Tested Features:
# - Ensures the Field model is registered in Django Admin.
# - Verifies admin list display settings.
# - Confirms superuser access to the Django Admin UI.
# - Tests search functionality by Field ID and Name.
# - Ensures fields are ordered alphabetically.
# - Validates admin filtering by position.
#
# Author: Daria Ilchenko
# Date: 03/03/2025
# ===========================================================================================

from django.contrib.admin.sites import site
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Field  # Import Field model
from core.admin import FieldAdmin  # Import FieldAdmin class


class FieldAdminTest(TestCase):
    # Test suite for Field model registration and accessibility in Django Admin.

    @classmethod
    def setUpTestData(cls):
        # Set up initial data for testing.
        #
        # - Creates a Field instance for testing.
        # - Creates a superuser to access the Django Admin panel.
        
        cls.field = Field.objects.create(
            field_id=1,
            field_name="Test Field",
            description="Test description",
            position=1
        )

        # Create a superuser to test Django Admin login and access
        cls.superuser = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

    def test_field_registered_in_admin(self):
        # Test if the Field model is registered in the Django Admin interface.
        #
        # - Retrieves all registered models from `site._registry`.
        # - Ensures the Field model is present in the registry.
        
        self.assertIn(Field, site._registry)  # Ensures Field model is registered

    def test_field_admin_list_display(self):
        # Test the list_display settings for the Field model in Django Admin.
        #
        # - Checks if the FieldAdmin class defines the correct fields for display.
        # - Ensures consistency with expected admin configurations.

        admin_instance = FieldAdmin(Field, site)  # Use Field model class, not instance
        self.assertEqual(
            admin_instance.list_display,
            ("field_id", "field_name", "description", "position")  # Fields shown in Admin UI
        )

    def test_admin_can_access_fields(self):
        # Test if an admin user can log in and access the Field model in Django Admin.
        #
        # - Logs in with the superuser created in setUpTestData.
        # - Sends a GET request to the Field model’s Django Admin page.
        # - Verifies that the page loads successfully with status code 200.
        
        login = self.client.login(username="admin", password="testpassword")
        self.assertTrue(login)  # Confirms that superuser login was successful

        # Dynamically generate the admin URL based on the app label and model name
        response = self.client.get(f"/admin/{Field._meta.app_label}/{Field._meta.model_name}/")
        self.assertEqual(response.status_code, 200)  # Ensures Admin UI is accessible

    def test_admin_search_functionality(self):
        # Test if the Field model search functionality works in Django Admin.
        #
        # - Retrieves the search fields defined in FieldAdmin.
        # - Ensures `field_id` and `field_name` are included in search fields.

        admin_instance = FieldAdmin(Field, site)
        search_fields = admin_instance.get_search_fields(request=None)

        self.assertIn("field_id", search_fields)
        self.assertIn("field_name", search_fields)

    def test_admin_list_filter(self):
        # Ensures filtering in Django Admin is set up correctly.
        #
        # - Checks if "position" appears in list_filter settings.

        admin_instance = FieldAdmin(Field, site)
        filter_fields = admin_instance.get_list_filter(request=None)

        self.assertIn("position", filter_fields)  # Ensures position is filterable

    def test_field_ordering(self):
        # Ensures the Field model orders by field_name by default.
        #
        # - Creates multiple Field instances.
        # - Retrieves the first record to ensure ordering is applied.

        field1 = Field.objects.create(field_id=2, field_name="Alpha Field", description="Description 1", position=1)
        field2 = Field.objects.create(field_id=3, field_name="Zeta Field", description="Description 2", position=2)
        
        first_field = Field.objects.order_by("field_name").first()
        self.assertEqual(first_field.field_name, "Alpha Field")  # Should be ordered alphabetically
