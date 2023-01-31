from configurations import values

from .base import ComposedProjectSettings


class Development(ComposedProjectSettings):
    """
    Settings for development environment.

    Intended to be used with ``make run`` for local development.
    """
    DEBUG = True

    # Don't send any email for real, just push them to the shell output
    EMAIL_BACKEND = values.Value("django.core.mail.backends.console.EmailBackend",
                                 environ_name="DJANGO_EMAIL_BACKEND")

    @classmethod
    def post_setup(cls):
        super().post_setup()

        # Expected path for optional Dotenv file
        cls.DOTENV = cls.BASE_DIR / ".env"

        # Disable webpack cache
        cls.WEBPACK_LOADER["DEFAULT"]["CACHE"] = values.BooleanValue(
            False,
            environ_name="WEBPACK_CACHE",
            environ_prefix=None
        )

        # Ensure the styleguide is updated during development
        cls.STYLEGUIDE_SAVE_DUMP = values.BooleanValue(
            True,
            environ_name="STYLEGUIDE_SAVE_DUMP",
            environ_prefix=None
        )

        # Force disabling error about Recaptcha API development keys
        if "captcha.recaptcha_test_key_error" not in cls.SILENCED_SYSTEM_CHECKS:
            cls.SILENCED_SYSTEM_CHECKS.append("captcha.recaptcha_test_key_error")
