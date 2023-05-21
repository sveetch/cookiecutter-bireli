from configurations import values

from .base import ComposedProjectSettings


class Test(ComposedProjectSettings):
    """
    Settings for test environment.

    Intended to be used only by test runner.
    """
    DEBUG = True

    # Don't send any email for real, just push them to the shell output
    EMAIL_BACKEND = values.Value("django.core.mail.backends.console.EmailBackend",
                                 environ_name="DJANGO_EMAIL_BACKEND")

    @classmethod
    def setup(cls):
        super().setup()

        cls.MEDIA_ROOT = cls.VAR_PATH / "media-tests"

    @classmethod
    def post_setup(cls):
        super(Test, cls).post_setup()

        # Disable webpack cache
        cls.WEBPACK_LOADER["DEFAULT"]["CACHE"] = values.BooleanValue(
            False,
            environ_name="WEBPACK_CACHE",
            environ_prefix=None,
        )

        # Patch database setting to use database in memory instead of file
        cls.DATABASES["default"]["NAME"] = values.Value(
            ":memory:",
            environ_name="DJANGO_DB_NAME",
            environ_prefix=None,
        )

        # Add page test templates if cms is enabled
        if hasattr(cls, "CMS_TEMPLATES"):
            cls.CMS_TEMPLATES += [
                (k, v)
                for k, v in cls.TEST_PAGE_TEMPLATES.items()
            ]

        # Force disabling error about Recaptcha API development keys
        if "captcha.recaptcha_test_key_error" not in cls.SILENCED_SYSTEM_CHECKS:
            cls.SILENCED_SYSTEM_CHECKS.append("captcha.recaptcha_test_key_error")
