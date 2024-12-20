from project_composer.marker import EnabledApplicationMarker


class DjangoTwoFactorAuthSettings(EnabledApplicationMarker):
    """
    Django two factor authentication
    """
    # All login are done through the Two factor form
    LOGIN_URL = "two_factor:login"

    # Override default Auth url redirects
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

        cls.MIDDLEWARE.append("django_otp.middleware.OTPMiddleware")
