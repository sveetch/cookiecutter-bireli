from configurations import values

from project_composer.marker import EnabledApplicationMarker


class DjangoAxesSettings(EnabledApplicationMarker):
    """
    Django Axes, login tracker and failure blocker
    """
    AXES_ENABLED = False
    AXES_ENABLE_ACCESS_FAILURE_LOG = True
    AXES_ENABLE_ADMIN = values.BooleanValue(True)
    AXES_FAILURE_LIMIT = values.PositiveIntegerValue(3)
    AXES_IPWARE_META_PRECEDENCE_ORDER = [
        "HTTP_X_FORWARDED_FOR",
        "REMOTE_ADDR",
    ]
    AXES_LOCKOUT_PARAMETERS = values.ListValue(["ip_address"])
    AXES_ONLY_ADMIN_SITE = values.BooleanValue(False)
    AXES_RESET_ON_SUCCESS = values.BooleanValue(True)
    AXES_VERBOSE = values.BooleanValue(False)

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.append("axes")

        cls.AUTHENTICATION_BACKENDS = [
            "axes.backends.AxesStandaloneBackend",
            "django.contrib.auth.backends.ModelBackend"
        ]

        cls.MIDDLEWARE.append("axes.middleware.AxesMiddleware")
