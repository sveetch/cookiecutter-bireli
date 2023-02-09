#!/usr/bin/env python
"""
Django management script
"""
import os
import sys
from pathlib import Path


if __name__ == "__main__":
    BASE_DIR = Path(__file__).parents[0].resolve()
    # Append django-apps to sys.path so apps in this directory are detected
    sys.path.append(
        str(BASE_DIR / "django-apps")
    )
    # Set the settings module to use where lives the environment settings classes
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Try to use the local environment settings if file exists
    if (BASE_DIR / "project" / "settings" / "localsettings.py").exists():
        os.environ.setdefault("DJANGO_CONFIGURATION", "LocalEnv")
    # Else set the default development environment settings
    else:
        os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
