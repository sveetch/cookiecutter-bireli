"""
========================
Django Sendfile settings
========================

"""
from configurations import values

from project_composer.marker import EnabledApplicationMarker


class SendfileSettings(EnabledApplicationMarker):
    """
    Django Sendfile
    """
    # Enabled sendfile backend
    SENDFILE_BACKEND = values.Value("django_sendfile.backends.simple")
    SENDFILE_URL = values.Value("/protected")

    @classmethod
    def setup(cls):
        super(SendfileSettings, cls).setup()

        cls.SENDFILE_ROOT = values.Value(cls.VAR_PATH / "protected-media")
