from project_composer.marker import EnabledApplicationMarker


class SearchSettings(EnabledApplicationMarker):
    """
    Django Haystack settings
    """

    HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

    @classmethod
    def setup(cls):
        super().setup()

        cls.HAYSTACK_CONNECTIONS = {
            "default": {
                "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
                "PATH": cls.PARTS_PATH / "whoosh" / "whoosh_index",
            },
        }

        cls.INSTALLED_APPS.extend([
            "haystack",
        ])
