from configurations import values

from project_composer.marker import EnabledApplicationMarker


class RecaptchaSettings(EnabledApplicationMarker):
    """
    Django reCAPTCHA settings
    """
    # These are API keys for localhost usage only, you must fill them right in
    # integration and production settings
    RECAPTCHA_PUBLIC_KEY = values.Value("6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI")
    RECAPTCHA_PRIVATE_KEY = values.Value("6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe")

    # For secure site, all captcha request will be in https
    # RECAPTCHA_USE_SSL = True

    @classmethod
    def setup(cls):
        super(RecaptchaSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "django_recaptcha",
        ])
