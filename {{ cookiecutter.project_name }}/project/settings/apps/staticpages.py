"""
===================================
emencia-django-staticpages settings
===================================

"""
from configurations import values


class StaticpageSettings:
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

    # Enabled staticpages configuration
    STATICPAGES = [
        "index",
    ]

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend([
            "staticpages.apps.staticpagesConfig",
        ])
