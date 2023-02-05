"""
===================================
emencia-django-staticpages settings
===================================

"""
from project_composer.marker import EnabledApplicationMarker


class StaticpageSettings(EnabledApplicationMarker):
    """
    Static pages
    """
    # Directory path (relative to a template directory path) where to search for
    # staticpage templates
    STATICPAGES_DEFAULT_TEMPLATEPATH = "prototypes"

    # Default view URL name prefix (would results to name "prototypes-mypage")
    STATICPAGES_DEFAULT_NAME_BASE = "prototypes-"

    # Base URL path for staticpage items (eg: "foo/bar" would results to
    # "/foo/bar/mypage/")
    STATICPAGES_DEFAULT_URLPATH = "prototypes"

    # URL name which qualify a staticpage as an index page.
    STATICPAGES_INDEX_NAME = 'index'

    # Enabled staticpages configuration
    STATICPAGES = [
        "index",
    ]

    @classmethod
    def setup(cls):
        super(StaticpageSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "staticpages.apps.staticpagesConfig",
        ])
