# ===========================================================================================
# CRUD Unit Tests for Table Model via Django ORM
# ===========================================================================================
# This test module verifies that an admin user can perform Create, Read, Update, and Delete
# operations on the Table model using the Django ORM. The tests simulate actions that would
# be done via the admin panel and ensure database integrity for core table metadata.
#
# Author: Zulfina Ivanova
# Date: 04/22/25
# ===========================================================================================

from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Table

class TableCRUDTest(TestCase):
    """Test suite to verify admin CRUD operations on the Table model."""

    @classmethod
    def setUpTestData(cls):
        # Create an admin user
        cls.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

        # Create an initial table record
        cls.initial_table = Table.objects.create(
            table_id=1,
            table_name="Test Table",
            description="This is a test table used for unit tests.",
            use_cases="Testing purposes.",
            important_notes="Ensure the table behaves as expected."
        )

    def test_create_table(self):
        """Admin can create a new Table record."""
        new_table = Table.objects.create(
            table_id=2,
            table_name="Analytics Table",
            description="Table for analytics data.",
            use_cases="Used in academic performance tracking.",
            important_notes="Populated weekly."
        )
        self.assertEqual(new_table.table_name, "Analytics Table")
        self.assertTrue(Table.objects.filter(table_name="Analytics Table").exists())

    def test_read_table(self):
        """Admin can read an existing Table record."""
        table = Table.objects.get(table_id=1)
        self.assertEqual(table.table_name, "Test Table")
        self.assertEqual(table.use_cases, "Testing purposes.")

    def test_update_table(self):
        """Admin can update an existing Table record."""
        table = Table.objects.get(table_id=1)
        table.important_notes = "Updated notes after feedback."
        table.save()

        updated_table = Table.objects.get(table_id=1)
        self.assertEqual(updated_table.important_notes, "Updated notes after feedback.")

    def test_delete_table(self):
        """Admin can delete a Table record."""
        temp_table = Table.objects.create(
            table_id=3,
            table_name="Temporary Table",
            description="Temp data",
            use_cases="None",
            important_notes="Delete after testing"
        )
        temp_table.delete()
        self.assertFalse(Table.objects.filter(table_id=3).exists())
