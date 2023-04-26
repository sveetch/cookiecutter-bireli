"""
==========================
Project utilities settings
==========================

"""
from project_composer.marker import EnabledApplicationMarker


class ProjectUtilsSettings(EnabledApplicationMarker):
    """
    Project utilities
    """

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
