"""
=====================
Django filer settings
=====================

"""
from project_composer.marker import EnabledApplicationMarker


class DjangoFilerSettings(EnabledApplicationMarker):
    """
    File browser solution
    """

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend([
            "easy_thumbnails",
            "filer",
            "mptt",
        ])
