from project_composer.marker import EnabledApplicationMarker


class DjangoAutocompleteSettings(EnabledApplicationMarker):
    """
    django-autocomplete-light (aka: DAL) settings. This app settings should be loaded
    just before "django.contrib.admin"
    """

    @classmethod
    def setup(cls):
        super(DjangoAutocompleteSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "dal",
            "dal_select2",
        ])
