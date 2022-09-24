#!/usr/bin/env python
"""
Django management script
"""
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    # Append django-apps to sys.path so apps in this directory are detected
    sys.path.append(
        str(Path(__file__).parents[0].resolve() / "django-apps")
    )
    # Set the default settings module to use
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    # Set the default settings configuration environment
    os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
