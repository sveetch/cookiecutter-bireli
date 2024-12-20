from configurations import values

from .base import ComposedProjectSettings


class Production(ComposedProjectSettings):
    """
    Settings for production environment.
    """
    # Labelize the deployed production environment name
    ENVIRONMENT = values.Value("Production", environ_name="DEPLOYED_ENVIRONMENT")

    # Mark environement as indexable
    SITE_INDEX_METAS = True

    # Enable Django Axes
    AXES_ENABLED = True

    # Set Django Axes lock on IP and username
    AXES_LOCKOUT_PARAMETERS = values.ListValue(["ip_address", "username"])

    # Create media path on volume
    @classmethod
    def setup(cls):
        super().setup()

        # Session cookie is only working on HTTPS
        cls.SESSION_COOKIE_SECURE = True
        # Session is lost once browser is closed
        cls.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        # CSRF cookie is only working on HTTPS
        cls.CSRF_COOKIE_SECURE = True
