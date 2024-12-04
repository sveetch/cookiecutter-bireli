from project_composer.marker import EnabledApplicationMarker


class LotusDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "lotus",
                {
                    "comments": "Lotus weblog",
                    "natural_foreign": True,
                    "models": "lotus",
                    "excludes": [
                        "lotus.Author",
                        "lotus.Article_authors",
                    ]
                }
            ],
        ]
