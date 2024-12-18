from project_composer.marker import EnabledApplicationMarker


class SendfileSettings(EnabledApplicationMarker):
    """
    Django Sendfile
    """
    # Enabled sendfile backend
    SENDFILE_BACKEND = "django_sendfile.backends.simple"
    SENDFILE_URL = "/protected"

    @classmethod
    def setup(cls):
        super(SendfileSettings, cls).setup()

        cls.SENDFILE_ROOT = cls.VAR_PATH / "protected-media"
