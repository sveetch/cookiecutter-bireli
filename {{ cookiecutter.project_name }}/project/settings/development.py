"""
====================================
Settings for development environment
====================================

Intended to be used with ``make run`` for local development.

"""
from project.settings.base import *  # noqa: F403

DEBUG = True

# Https is disabled on development environment
HTTPS_ENABLED = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": VAR_PATH / "db" / "db.sqlite3",  # noqa: F405
    }
}

# In development, not any email is really sent to a SMTP server,
# instead they are just outputted to your terminal console where
# Django runserver is running.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


"""
Django Webpack settings
"""
# Disable cache to avoid reloading Django instance to get new bundle builds
WEBPACK_LOADER["DEFAULT"]["CACHE"] = False  # noqa: F405


# Import optionnal local settings for local overriding
try:
    from .local import *  # noqa: F401,F403
except ImportError:
    pass
