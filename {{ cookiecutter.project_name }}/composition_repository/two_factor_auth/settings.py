from project_composer.marker import EnabledApplicationMarker


class DjangoTwoFactorAuthSettings(EnabledApplicationMarker):
    """
    Django two factor authentication
    """

    LOGIN_URL = "two_factor:login"

    # this one is optional
    LOGIN_REDIRECT_URL = "two_factor:profile"
    LOGOUT_REDIRECT_URL = "two_factor:login"

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend(
            [
                "django_otp",
                "django_otp.plugins.otp_static",
                "django_otp.plugins.otp_totp",
                "django_otp.plugins.otp_email",
                "two_factor",
                "two_factor.plugins.email",
            ]
        )

        cls.MIDDLEWARE.extend(["django_otp.middleware.OTPMiddleware"])
