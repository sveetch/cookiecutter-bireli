from project_composer.marker import EnabledApplicationMarker


class ProjectUtilsSettings(EnabledApplicationMarker):
    """
    Project utilities
    """
    # Internal mark to know if site expose meta elements for real indexation. This is
    # should commonly be enabled only for production environment. This is not related
    # to context processor "site_metas".
    SITE_INDEX_METAS = False

    # To include extra data in context processor "site_metas". Content will be
    # available in 'EXTRA' context variable.
    EXTRA_SITE_METAS = None

    @classmethod
    def setup(cls):
        super(ProjectUtilsSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "project_utils",
        ])

        # Basic processor to insert some common global variables
        cls.TEMPLATES[0]["OPTIONS"]["context_processors"].extend([
            "project_utils.context_processors.site_metas",
        ])
