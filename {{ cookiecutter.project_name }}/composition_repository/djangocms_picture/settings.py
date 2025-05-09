from django.utils.translation import gettext_lazy as _

from project_composer.marker import EnabledApplicationMarker


class DjangocmsPictureSettings(EnabledApplicationMarker):
    """
    djangocms-picture settings
    """
    DJANGOCMS_PICTURE_ALIGN = (
        ("picture-left", _("Align left")),
        ("picture-center", _("Align center")),
        ("picture-right", _("Align right")),
    )

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.append("djangocms_picture")
