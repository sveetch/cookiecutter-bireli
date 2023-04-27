from project_composer.marker import EnabledApplicationMarker

from lotus.contrib.django_configuration import LotusDefaultSettings


class LotusSettings(LotusDefaultSettings, EnabledApplicationMarker):
    """
    Lotus settings
    """

    @classmethod
    def setup(cls):
        super(LotusSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "view_breadcrumbs",
            "lotus",
        ])
