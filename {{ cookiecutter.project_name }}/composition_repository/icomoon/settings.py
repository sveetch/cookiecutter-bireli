"""
=======================
Django Icomoon settings
=======================

"""
from project_composer.marker import EnabledApplicationMarker


class IcomoonSettings(EnabledApplicationMarker):
    """
    Icomoon font icon manager
    """
    ICOMOON_CSS_TEMPLATE = "icomoon/icon_map.scss"

    @classmethod
    def setup(cls):
        super(IcomoonSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "icomoon",
        ])

        cls.ICOMOON_WEBFONTS = {
            "Default": {
                "fontdir_path": cls.PROJECT_PATH / "static-sources" / "fonts/icons",
                "csspart_path": (
                    cls.PROJECT_PATH, "frontend/scss/settings/_icomoon_icons.scss"
                ),
            }
        }
