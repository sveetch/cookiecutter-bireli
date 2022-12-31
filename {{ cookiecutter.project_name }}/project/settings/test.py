"""
================
Test environment
================

"""
from configurations import values

from .development import Development


class Test(Development):
    """
    Settings for test environment.

    Intended to be used only by test runner.
    """
    @property
    def MEDIA_ROOT(self):
        """
        Media directory dedicated to tests to avoid polluting other environment
        media directory
        """
        return self.VAR_PATH / "media-tests"

    @classmethod
    def post_setup(cls):
        super().post_setup()

        # Patch database setting to use database in memory instead of file
        cls.DATABASES["default"]["NAME"] = values.Value(
            ":memory:",
            environ_name="DJANGO_DB_NAME",
            environ_prefix=None
        )

        # Add page test templates if cms is enabled
        if hasattr(cls, "CMS_TEMPLATES"):
            cls.CMS_TEMPLATES += [
                (k, v)
                for k, v in cls.TEST_PAGE_TEMPLATES.items()
            ]
