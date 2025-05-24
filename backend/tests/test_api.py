# ===========================================================================================
# API Tests for Seamless Data Retrieval
# ===========================================================================================
# This module contains test cases for verifying API updates for retrieving tables, fields, 
# labels, and entries while ensuring proper filtering and ordering.
#
# Tested Features:
# - API response validation for tables, fields, labels, and entries.
# - Ensure filtering and search functionality works.
# - Verify correct ordering of results.
# - Ensure consistency between API & Django Admin data.
#
# Author: Daria Ilchenko
# Date: 03/07/2025
# ===========================================================================================

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Table, Field, Label, Entry


class APITestCaseSeamlessDataRetrieval(APITestCase):
    
    # API test suite for verifying seamless data retrieval.

    @classmethod
    def setUpTestData(cls):
        
        # Set up initial test data for API tests.
        
        # Create a Table instance
        cls.table = Table.objects.create(
            table_id=1,
            table_name="Test Table",
            description="Test description",
            use_cases="Test use cases",
            important_notes="Test notes"
        )

        # Create a Field instance linked to the Table
        cls.field = Field.objects.create(
            field_id=1,
            field_name="Test Field",
            description="Test Field Description",
            position=1
        )
        cls.field.tables.add(cls.table)  # ManyToMany relationship setup

        # Create a Label instance linked to the Table
        cls.label = Label.objects.create(
            label_id=1,
            label_name="Test Label",
            label_index=10,
            table_id=cls.table
        )

        # Create an Entry instance linked to the Field and Label
        cls.entry = Entry.objects.create(
            entry_id=1,
            entry_content="Test Entry Content",
            field=cls.field,
            label=cls.label
        )

        # Create a superuser for API access
        cls.superuser = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="testpassword"
        )

    def setUp(self):
        
        # Authenticate the test client as the superuser.
        
        self.client.login(username="admin", password="testpassword")

    # ---------------------------------------------------------------------------------------
    # TEST API RETRIEVAL (Ensure API Returns Tables, Fields, Labels, Entries)
    # ---------------------------------------------------------------------------------------

    def test_api_retrieves_tables(self):
        # Ensure API correctly retrieves tables.
        response = self.client.get("/api/tables/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["table_name"], "Test Table")

    def test_api_retrieves_fields(self):
        # Ensure API correctly retrieves fields.
        response = self.client.get("/api/fields/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["field_name"], "Test Field")

    def test_api_retrieves_labels(self):
        # Ensure API correctly retrieves labels.
        response = self.client.get("/api/labels/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["label_name"], "Test Label")

    def test_api_retrieves_entries(self):
        # Ensure API correctly retrieves entries.
        response = self.client.get("/api/entries/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["entry_content"], "Test Entry Content")

    # ---------------------------------------------------------------------------------------
    # TEST FILTERS & ORDERING
    # ---------------------------------------------------------------------------------------

    def test_api_filters_labels_by_table(self):
        # Ensure API can filter labels by associated table.
        response = self.client.get(f"/api/labels/?table_id={self.table.table_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["label_name"], "Test Label")

    def test_api_filters_entries_by_label(self):
        # Ensure API can filter entries by associated label.
        response = self.client.get(f"/api/entries/?label_id={self.label.label_id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["entry_content"], "Test Entry Content")

    def test_api_orders_labels_by_name(self):
        # Ensure API orders labels by name correctly.
        Label.objects.create(label_id=2, label_name="Alpha Label", label_index=5, table_id=self.table)
        response = self.client.get("/api/labels/?ordering=label_name")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["label_name"], "Alpha Label")

    # ---------------------------------------------------------------------------------------
    # TEST API ERROR HANDLING & DATA CONSISTENCY
    # ---------------------------------------------------------------------------------------

    def test_api_returns_404_for_nonexistent_table(self):
        # Ensure API returns 404 for a non-existent table.
        response = self.client.get("/api/tables/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_consistency_with_admin(self):
        # Ensure API returns the same data as Django Admin.
        admin_response = self.client.get("/admin/core/label/")
        api_response = self.client.get("/api/labels/")
        self.assertEqual(len(admin_response.context["cl"].queryset), len(api_response.data))
