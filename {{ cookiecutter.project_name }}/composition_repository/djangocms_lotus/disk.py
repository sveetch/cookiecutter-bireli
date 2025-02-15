from project_composer.marker import EnabledApplicationMarker


class CmsLotusDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "djangocms_lotus",
                {
                    "comments": "Lotus for DjangoCMS",
                    "natural_foreign": True,
                    "models": "djangocms_lotus",
                }
            ],
        ]
