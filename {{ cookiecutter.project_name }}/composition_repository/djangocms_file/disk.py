from project_composer.marker import EnabledApplicationMarker


class DjangoCmsFileDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "djangocms_file",
                {
                    "comments": "Djangocms_File",
                    "natural_foreign": True,
                    "models": "djangocms_file",
                }
            ],
        ]
