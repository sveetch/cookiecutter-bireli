from project_composer.marker import EnabledApplicationMarker


class DjangoDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "django.contrib.auth",
                {
                    "comments": "Authentication and Authorization",
                    "natural_foreign": True,
                    "models": ["auth.User", "auth.Group"],
                }
            ],
            [
                "django.contrib.sites",
                {
                    "comments": "Sites",
                    "natural_foreign": True,
                    "models": "sites",
                }
            ],
        ]
