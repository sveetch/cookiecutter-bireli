from project_composer.marker import EnabledApplicationMarker

from smart_media.contrib.django_configuration import SmartMediaDefaultSettings


class SmartMediaSettings(SmartMediaDefaultSettings, EnabledApplicationMarker):
    """
    Smart Media and Sorl settings

    It is important than Sorl is installed BEFORE django-filer, since filer includes
    easy-thumbnail which use the same template tag library. Else they would conflict,
    template using the easy-thumbnail would raise exception due to invalid argument
    syntax against the sorl tag.
    """
    SMART_FORMAT_AVAILABLE_FORMATS = [
        ("jpg", "JPEG"),
        ("jpeg", "JPEG"),
        ("png", "PNG"),
        ("gif", "GIF"),
        ("svg", "SVG"),
    ]
    """
    Available formats for template tag ``media_thumb``.
    """

    @classmethod
    def setup(cls):
        super(SmartMediaSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "sorl.thumbnail",
            "smart_media",
        ])
