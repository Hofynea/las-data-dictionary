"""
apps.py

This module defines the application configuration for the 'core' app
in the L@S Data Dictionary project.

The CoreConfig class sets the default auto field type for models and
registers the app under the name 'core'.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
