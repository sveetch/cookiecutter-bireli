"""
=============================
Settings for test environment
=============================

Intended to be used only by test runner.

"""

from project.settings.base import *  # noqa: F403

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "TEST": {
            "NAME": VAR_PATH / "db" / "tests.sqlite3",  # noqa: F405
        }
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Media directory dedicated to tests to avoid polluting other environment
# media directory
MEDIA_ROOT = VAR_PATH / "media-tests"  # noqa: F405
