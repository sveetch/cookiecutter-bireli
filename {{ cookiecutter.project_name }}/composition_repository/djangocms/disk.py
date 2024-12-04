from project_composer.marker import EnabledApplicationMarker


class CmsDefinitions(EnabledApplicationMarker):
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
                "djangocms_picture",
                {
                    "comments": "Djangocms_Picture",
                    "natural_foreign": True,
                    "models": "djangocms_picture",
                }
            ],
            [
                "djangocms_snippet",
                {
                    "comments": "Snippets",
                    "natural_foreign": True,
                    "models": "djangocms_snippet",
                }
            ],
            [
                "djangocms_text_ckeditor",
                {
                    "comments": "django CMS Text CKEditor",
                    "natural_foreign": True,
                    "models": "djangocms_text_ckeditor",
                }
            ],
            # All CMS plugin configs must comes after DjangoCMS else the dump will be
            # broken for loading.
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
