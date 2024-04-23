from project_composer.marker import EnabledApplicationMarker


class ProjectUtilsSettings(EnabledApplicationMarker):
    """
    Project utilities
    """
    # Internal mark to know if site expose meta elements for real indexation. This is
    # should commonly be enabled only for production environment. This is not related
    # to context processor "project_globals".
    SITE_INDEX_METAS = False

    # To include extra data in context processor "project_globals". Content will be
    # available in 'EXTRA' context variable.
    EXTRA_PROJECT_GLOBALS = None

    @classmethod
    def setup(cls):
        super(ProjectUtilsSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "project_utils",
        ])

        # Processor to add some common global variables in template context
        cls.TEMPLATES[0]["OPTIONS"]["context_processors"].extend([
            "project_utils.context_processors.project_globals",
        ])
