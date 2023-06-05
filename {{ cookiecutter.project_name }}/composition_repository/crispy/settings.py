from project_composer.marker import EnabledApplicationMarker


class CrispyFormSettings(EnabledApplicationMarker):
    """
    django-crispy-forms settings
    """

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

    CRISPY_TEMPLATE_PACK = "bootstrap5"

    @classmethod
    def setup(cls):
        super(CrispyFormSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "crispy_forms",
            "crispy_bootstrap5",
        ])
