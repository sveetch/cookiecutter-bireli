from project_composer.marker import EnabledApplicationMarker


class SitemapsSettings(EnabledApplicationMarker):
    """
    Sitemaps settings
    """
    @classmethod
    def setup(cls):
        super(SitemapsSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "django.contrib.sitemaps",
            "project_sitemaps",
        ])
