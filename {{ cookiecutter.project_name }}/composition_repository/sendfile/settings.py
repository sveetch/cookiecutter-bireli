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
    SENDFILE_BACKEND = values.Value("django_sendfile.backends.simple",
                                    environ_name="SENDFILE_BACKEND")
    SENDFILE_URL = values.Value("/protected", environ_name="SENDFILE_URL")

    @classmethod
    def setup(cls):
        super().setup()

        cls.SENDFILE_ROOT = values.Value(cls.VAR_PATH / "protected-media",
                                         environ_name="SENDFILE_ROOT")
