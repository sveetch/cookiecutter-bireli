"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Development")

application = get_wsgi_application()
