from project_composer.marker import EnabledApplicationMarker


class TaggitDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "taggit",
                {
                    "comments": "Taggit",
                    "natural_foreign": True,
                    "models": "taggit",
                }
            ],
        ]
