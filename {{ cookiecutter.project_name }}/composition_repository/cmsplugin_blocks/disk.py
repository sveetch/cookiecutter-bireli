from project_composer.marker import EnabledApplicationMarker


class CmsPluginBlocksDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "cmsplugin_blocks",
                {
                    "comments": "CMS Blocks",
                    "natural_foreign": True,
                    "models": "cmsplugin_blocks",
                }
            ],
        ]
