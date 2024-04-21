from project_composer.marker import EnabledApplicationMarker


class LotusDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "lotus",
                {
                    "comments": "Lotus weblog",
                    "natural_foreign": True,
                    "models": [
                        "lotus.Album",
                        "lotus.AlbumItem",
                        "lotus.Article_categories",
                        "lotus.Article_related",
                        "lotus.Article",
                        "lotus.Category"
                    ],
                    "excludes": [
                        "lotus.Author",
                        "lotus.Article_authors",
                    ]
                }
            ],
        ]
