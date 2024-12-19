from project_composer.marker import EnabledApplicationMarker


class CmsDefinitions(EnabledApplicationMarker):
    """
    .. Warning::
        All CMS plugin configs must comes after DjangoCMS else the dump will be
        broken for loading.
    """
    def define(self):
        return super().define() + [
            [
                "cms",
                {
                    "comments": "django CMS",
                    "natural_foreign": True,
                    "models": "cms",
                }
            ],
            [
                "menus",
                {
                    "comments": "django CMS menus system",
                    "natural_foreign": True,
                    "models": "menus",
                }
            ],
            [
                "djangocms_text",
                {
                    "comments": "django CMS Text",
                    "natural_foreign": True,
                    "models": "djangocms_text",
                }
            ],
            # These plugins are currently disabled until official support for
            # DjangoCMS 4
            # [
            #     "djangocms_picture",
            #     {
            #         "comments": "Djangocms_Picture",
            #         "natural_foreign": True,
            #         "models": "djangocms_picture",
            #     }
            # ],
            # [
            #     "djangocms_snippet",
            #     {
            #         "comments": "Snippets",
            #         "natural_foreign": True,
            #         "models": "djangocms_snippet",
            #     }
            # ],
            # Fobi is deprecated as well as its plugin
            # [
            #     "fobi.contrib.apps.djangocms_integration",
            #     {
            #         "comments": "Fobi_Contrib_Apps_Djangocms_Integration",
            #         "natural_foreign": True,
            #         "models": [
            #             "fobi_contrib_apps_djangocms_integration.FobiFormWidget"
            #         ]
            #     }
            # ],
        ]
