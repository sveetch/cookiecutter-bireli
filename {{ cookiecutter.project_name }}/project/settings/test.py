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

        # Created media from tests are done in another directory so it can be flushed
        # without removing media from local development
        cls.MEDIA_ROOT = cls.VAR_PATH / "media-tests"

        # Specifically defines this here because we can not override it inside
        # tests
        cls.REQUEST_SUBJECTS = {
            "ENTREPRISE": {
                "label": "Entreprise",
                "recipients": ["Entreprise@localhost"],
            },
            "NOPE": {
                "label": "Nope",
            },
        }

        # All test are written for english language
        cls.LANGUAGE_CODE = "en"
        # Ensure english language is available
        if "en" not in [k for k, v in cls.LANGUAGES]:
            cls.LANGUAGES = cls.LANGUAGES + (("en", "English"),)

        # Disable Recaptcha because the V3 does not support development keys and would
        # make the tests to fail
        cls.REQUEST_FORM_DISABLE_CAPTCHA = True

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
                (v, k)
                for k, v in cls.TEST_PAGE_TEMPLATES.items()
            ]

        # Force disabling error about Recaptcha API development keys
        flag_name = "django_recaptcha.recaptcha_test_key_error"
        if flag_name not in cls.SILENCED_SYSTEM_CHECKS:
            cls.SILENCED_SYSTEM_CHECKS.append(flag_name)
