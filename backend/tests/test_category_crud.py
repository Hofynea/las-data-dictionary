# ===========================================================================================
# CRUD Unit Tests for Category Model via Django ORM
# ===========================================================================================
# This module contains unit test cases that verify the ability of an admin user to perform
# CRUD (Create, Read, Update, Delete) operations on the Category model.
#
# Tested Features:
# - Admin can create a new Category
# - Admin can retrieve an existing Category
# - Admin can update a Category
# - Admin can delete a Category
#
# Author: Daria Ilchenko
# Date: 04/18/2025
# ===========================================================================================

from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Category

class CategoryCRUDTest(TestCase):
    # Test suite for admin-level CRUD operations on the Category model.

    @classmethod
    def setUpTestData(cls):
        # Set up initial data and superuser.
        cls.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )
        cls.initial_category = Category.objects.create(
            category_id=1,
            category_name="Initial Category"
        )

    def test_create_category(self):
        # Verifies that a Category can be created successfully using ORM.
        category = Category.objects.create(
            category_id=2,
            category_name="Created Category"
        )
        self.assertEqual(category.category_name, "Created Category")
        self.assertTrue(Category.objects.filter(category_name="Created Category").exists())

    def test_read_category(self):
        # Verifies that an existing Category can be retrieved.
        category = Category.objects.get(category_id=1)
        self.assertEqual(category.category_name, "Initial Category")

    def test_update_category(self):
        # Verifies that a Category can be updated using ORM.
        category = Category.objects.get(category_id=1)
        category.category_name = "Updated Category"
        category.save()

        updated = Category.objects.get(category_id=1)
        self.assertEqual(updated.category_name, "Updated Category")

    def test_delete_category(self):
        # Verifies that a Category can be deleted and is no longer in the database.
        category = Category.objects.create(
            category_id=3,
            category_name="Temp Category"
        )
        category.delete()
        self.assertFalse(Category.objects.filter(category_id=3).exists())
        