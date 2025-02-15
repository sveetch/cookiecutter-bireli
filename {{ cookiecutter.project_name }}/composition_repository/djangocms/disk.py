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
                    "use_base_manager": True,
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
            [
                "djangocms_versioning",
                {
                    "comments": "DjangoCMS versionning",
                    "natural_foreign": True,
                    "models": "djangocms_versioning",
                }
            ],
            [
                "djangocms_alias",
                {
                    "comments": "DjangoCMS aliases",
                    "natural_foreign": True,
                    "models": "djangocms_alias",
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
            # NOTE: Uncomment this block if you enabled Request form from composer
            # [
            #     "request_form",
            #     {
            #         "comments": "Request form app",
            #         "natural_foreign": True,
            #         "models": "request_form",
            #     }
            # ],
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
        ]
