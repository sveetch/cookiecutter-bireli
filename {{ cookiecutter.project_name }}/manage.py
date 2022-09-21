#!/usr/bin/env python
"""
Django management script
"""
import os
import sys
from pathlib import Path

from django.core import management

if __name__ == "__main__":
    # Append django-apps to sys.path so apps in this directory are detected
    sys.path.append(
        str(Path(__file__).parents[0].resolve() / "django-apps")
    )
    # Set the default settings module to use if not explicitely given as argument
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.development")

    management.execute_from_command_line()
