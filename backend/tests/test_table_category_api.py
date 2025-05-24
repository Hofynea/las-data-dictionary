# ===========================================================================================
# API Tests for Table Filtering by Category
# ===========================================================================================
# This module contains test cases to validate the backend API's ability to filter `Table` 
# data by `Category` via query parameters.
#
# Tested Features:
# - Filtering by a valid category name (case-insensitive).
# - Handling non-existent category names gracefully.
# - Returning all tables when no category filter is applied.
#
# Endpoint Tested:
# - `/api/tables/?category=...`
#
# Author: Daria Ilchenko
# Date: 03/25/2025
# ===========================================================================================

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Table, Category, Label


@pytest.mark.django_db
class TestTableCategoryAPI:
    # Test suite for filtering tables by category through the TableWithFieldsView API.

    @pytest.fixture
    def setup_data(self):
        # Set up initial test data:
        # - Creates two categories.
        # - Creates two tables.
        # - Links each table to a category via a label.

        category_enroll = Category.objects.create(category_name="Enrollment")
        category_tech = Category.objects.create(category_name="Technology")

        table_1 = Table.objects.create(
            table_id=101,
            table_name="Course Enrollment Data",
            description="Student course registrations",
            use_cases="Track academic load",
            important_notes="Includes drop/add periods"
        )

        table_2 = Table.objects.create(
            table_id=102,
            table_name="Device Usage",
            description="Tracks mobile usage patterns",
            use_cases="User engagement",
            important_notes="Aggregated data"
        )

        Label.objects.create(
            label_name="Enrollment Term",
            label_index=0,
            table_id=table_1,
            category=category_enroll
        )

        Label.objects.create(
            label_name="Usage Count",
            label_index=0,
            table_id=table_2,
            category=category_tech
        )

    def test_filter_tables_by_valid_category(self, setup_data):
        # Validates that filtering by an existing category name returns the correct table(s).
        #
        # Expected Behavior:
        # - 200 OK response
        # - Contains one table related to the "Enrollment" category

        client = APIClient()
        url = reverse("table-list")
        response = client.get(url, {"category": "Enrollment"})

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)
        assert len(response.data) == 1
        assert response.data[0]["table_name"] == "Course Enrollment Data"

    def test_filter_tables_by_invalid_category(self, setup_data):
        # Ensures that filtering by a non-existent category returns an empty list.
        #
        # Expected Behavior:
        # - 200 OK response
        # - Empty result set

        client = APIClient()
        url = reverse("table-list")
        response = client.get(url, {"category": "NonexistentCategory"})

        assert response.status_code == status.HTTP_200_OK
        assert response.data == []

    def test_filter_tables_without_category(self, setup_data):
        # Verifies that when no category filter is applied, all tables are returned.
        #
        # Expected Behavior:
        # - 200 OK response
        # - Returns all created tables (2 total)

        client = APIClient()
        url = reverse("table-list")
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
