from project_composer.marker import EnabledApplicationMarker

from cmsplugin_blocks.contrib.django_configuration import CmsBlocksDefaultSettings


class CmsPluginBlocksSettings(CmsBlocksDefaultSettings, EnabledApplicationMarker):
    """
    cmsplugin-blocks settings
    """

    @classmethod
    def setup(cls):
        super(CmsPluginBlocksSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "cmsplugin_blocks",
        ])
