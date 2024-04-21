from project_composer.marker import EnabledApplicationMarker


class CmsPluginBlocksDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "cmsplugin_blocks",
                {
                    "comments": "CMS Blocks",
                    "natural_foreign": True,
                    "models": [
                        "cmsplugin_blocks.Album",
                        "cmsplugin_blocks.AlbumItem",
                        "cmsplugin_blocks.Card",
                        "cmsplugin_blocks.Container",
                        "cmsplugin_blocks.Hero",
                        "cmsplugin_blocks.Slider",
                        "cmsplugin_blocks.SlideItem"
                    ]
                }
            ],
        ]
