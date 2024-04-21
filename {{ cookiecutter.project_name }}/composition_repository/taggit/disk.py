from project_composer.marker import EnabledApplicationMarker


class TaggitDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "taggit",
                {
                    "comments": "Taggit",
                    # Taggit clearly don't support natural key, see
                    # django-taggit/issues/708
                    "natural_foreign": False,
                    "models": [
                        "taggit.Tag",
                        "taggit.TaggedItem"
                    ]
                }
            ],
        ]
