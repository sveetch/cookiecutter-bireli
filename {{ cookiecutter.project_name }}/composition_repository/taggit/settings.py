from project_composer.marker import EnabledApplicationMarker


class TaggitSettings(EnabledApplicationMarker):
    """
    django-taggit settings
    """

    @classmethod
    def setup(cls):
        super(TaggitSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "taggit",
        ])
