from project_composer.marker import EnabledApplicationMarker


class DjangoFilerDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            # TODO: Not sure this is useful, check and validate it
            [
                "easy_thumbnails",
                {
                    "comments": "Easy_Thumbnails",
                    "natural_foreign": True,
                    "models": [
                        "easy_thumbnails.Source",
                        "easy_thumbnails.Thumbnail",
                        "easy_thumbnails.ThumbnailDimensions"
                    ]
                }
            ],
            [
                "filer",
                {
                    "comments": "Filer",
                    "natural_foreign": True,
                    "dump_command": "polymorphic_dumpdata",
                    "models": [
                        "filer.Folder",
                        "filer.FolderPermission",
                        "filer.File",
                        "filer.Clipboard",
                        "filer.ClipboardItem",
                        "filer.Image",
                        "filer.ThumbnailOption"
                    ]
                }
            ],
        ]
