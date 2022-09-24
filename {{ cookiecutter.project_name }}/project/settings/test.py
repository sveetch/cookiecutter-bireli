"""
================
Test environment
================

"""
from .development import ComposedProjectSettings


class Test(ComposedProjectSettings):
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

        # Patch database setting to use an independent database
        cls.DATABASES["default"]["NAME"] = ":memory:"
        cls.DATABASES["default"]["TEST"] = {
            "NAME": cls.VAR_PATH / "db" / "tests.sqlite3",
        }
