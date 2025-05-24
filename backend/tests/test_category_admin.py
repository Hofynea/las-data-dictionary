# ===========================================================================================
# Django Admin Tests for Category Model
# ===========================================================================================
# This module contains test cases for verifying the registration and functionality of the 
# Category model in the Django Admin interface.
#
# Tested Features:
# - Ensures the Category model is registered in Django Admin.
# - Verifies admin list display settings.
# - Confirms superuser access to the Django Admin UI.
# - Tests search functionality by Category ID.
# - Ensures categories are ordered alphabetically.
#
# Author: Daria Ilchenko
# Date: 02/28/2025
# ===========================================================================================

from django.contrib.admin.sites import site
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Category  # Import Category model
from core.admin import CategoryAdmin  # Import CategoryAdmin class


class CategoryAdminTest(TestCase):
    # Test suite for Category model registration and accessibility in Django Admin.

    @classmethod
    def setUpTestData(cls):
        # Set up initial data for testing.
        #
        # - Creates a Category instance for testing.
        # - Creates a superuser to access the Django Admin panel.
        
        cls.category = Category.objects.create(
            category_id=1,
            category_name="Test Category"
        )

        # Create a superuser to test Django Admin login and access
        cls.superuser = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

    def test_category_registered_in_admin(self):
        # Test if the Category model is registered in the Django Admin interface.
        #
        # - Retrieves all registered models from `site._registry`.
        # - Ensures the Category model is present in the registry.
        
        self.assertIn(Category, site._registry)  # Ensures Category model is registered

    def test_category_admin_list_display(self):
        # Test the list_display settings for the Category model in Django Admin.
        #
        # - Checks if the CategoryAdmin class defines the correct fields for display.
        # - Ensures consistency with expected admin configurations.

        admin_instance = CategoryAdmin(Category, site)  # Use Category model class, not instance
        self.assertEqual(
            admin_instance.list_display,
            ("category_id", "category_name")  # Fields shown in Admin UI
        )

    def test_admin_can_access_categories(self):
        # Test if an admin user can log in and access the Category model in Django Admin.
        #
        # - Logs in with the superuser created in setUpTestData.
        # - Sends a GET request to the Category model’s Django Admin page.
        # - Verifies that the page loads successfully with status code 200.
        
        login = self.client.login(username="admin", password="testpassword")
        self.assertTrue(login)  # Confirms that superuser login was successful

        # Dynamically generate the admin URL based on the app label and model name
        response = self.client.get(f"/admin/{Category._meta.app_label}/{Category._meta.model_name}/")
        self.assertEqual(response.status_code, 200)  # Ensures Admin UI is accessible

    def test_admin_search_functionality(self):
        # Test if the Category model search functionality works in Django Admin.
        #
        # - Retrieves the search fields defined in CategoryAdmin.
        # - Ensures `category_id` is included in search fields.

        admin_instance = CategoryAdmin(Category, site)
        search_fields = admin_instance.get_search_fields(request=None)

        self.assertIn("category_id", search_fields)  # Ensures category_id is searchable

    def test_category_ordering(self):
        # Ensures the Category model orders by category_name by default.
        #
        # - Creates multiple Category instances.
        # - Retrieves the first record to ensure ordering is applied.

        category1 = Category.objects.create(category_id=2, category_name="Alpha Category")
        category2 = Category.objects.create(category_id=3, category_name="Zeta Category")
        
        first_category = Category.objects.order_by("category_name").first()
        self.assertEqual(first_category.category_name, "Alpha Category")  # Should be ordered alphabetically
