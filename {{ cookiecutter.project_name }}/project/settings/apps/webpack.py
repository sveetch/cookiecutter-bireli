"""
==============================
Django Webpack loader settings
==============================

"""
from configurations import values


class WebpackModSettings:
    """
    Django Webpack plugin settings

    Cache is enabled by default since deployed instances are always reloaded and we don't
    build frontend again until next deployment. However local development will have to
    disable it else django-webpack will use the first encountered bundle hash until next
    instance reload.
    """
    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend([
            "webpack_loader",
        ])

        cls.WEBPACK_LOADER = {
            "DEFAULT": {
                "CACHE": values.BooleanValue(
                    True,
                    environ_name="WEBPACK_CACHE",
                    environ_prefix=None
                ),
                "STATS_FILE": cls.PROJECT_PATH / "static-sources" / "webpack-stats.json",
                "POLL_INTERVAL": 0.1,
                "IGNORE": [r".+\.hot-update.js", r".+\.map"],
            }
        }
