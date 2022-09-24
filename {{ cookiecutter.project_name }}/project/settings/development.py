"""
=======================
Development environment
=======================

"""
from .base import ComposedProjectSettings


class Development(ComposedProjectSettings):
    """
    Settings for development environment.

    Intended to be used with ``make run`` for local development.
    """
    DEBUG = True

    # Https is disabled on development environment
    HTTPS_ENABLED = False

    # Don't send any email for real, just push them to the shell output
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    @classmethod
    def post_setup(cls):
        super().post_setup()

        # Disable webpack cache
        cls.WEBPACK_LOADER["DEFAULT"]["CACHE"] = False
