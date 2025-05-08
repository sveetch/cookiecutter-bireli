from configurations import values

from project_composer.marker import EnabledApplicationMarker


class RecaptchaSettings(EnabledApplicationMarker):
    """
    Django reCAPTCHA settings
    """
    RECAPTCHA_PUBLIC_KEY = values.Value("publickey")
    RECAPTCHA_PRIVATE_KEY = values.Value("secretkey")

    # On default the Captcha requests are done with HTTPS but you may try to use HTTP
    # instead (this is not recommended).
    # RECAPTCHA_USE_SSL = False

    @classmethod
    def setup(cls):
        super(RecaptchaSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "django_recaptcha",
        ])
