"""
==============================
Django Webpack loader settings
==============================

"""
from configurations import values

from project_composer.marker import EnabledApplicationMarker


class WebpackSettings(EnabledApplicationMarker):
    """
    Django Webpack plugin settings

    Cache is enabled by default since deployed instances are always reloaded and we
    don't build frontend again until next deployment. However local development will
    have to disable it else django-webpack will use the first encountered bundle hash
    until next instance reload.
    """
    @classmethod
    def setup(cls):
        super(WebpackSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "webpack_loader",
        ])

        cls.WEBPACK_LOADER = {
            "DEFAULT": {
                "CACHE": values.BooleanValue(
                    True,
                    environ_name="WEBPACK_CACHE",
                ),
                "STATS_FILE": (
                    cls.PARTS_PATH / "webpack" / "webpack-stats.json"
                ),
                "POLL_INTERVAL": 0.1,
                "IGNORE": [r".+\.hot-update.js", r".+\.map"],
            }
        }
