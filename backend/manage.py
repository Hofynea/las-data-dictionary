"""
manage.py

This is the command-line utility for administrative tasks in the L@S Data Dictionary project.
It sets the default settings module and delegates command execution to Django’s management tools.

Typical Usage:
- Running the development server
- Applying migrations
- Creating superusers
- Running custom mana ement commands

This file should not be modified unless changing the project's settings entry point.
"""


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
