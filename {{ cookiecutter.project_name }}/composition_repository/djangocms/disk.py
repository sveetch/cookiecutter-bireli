from project_composer.marker import EnabledApplicationMarker


class CmsDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "cms",
                {
                    "comments": "django CMS",
                    "natural_foreign": True,
                    "models": [
                        "cms.UserSettings",
                        "cms.TreeNode",
                        "cms.Page_placeholders",
                        "cms.Page",
                        "cms.PageType",
                        "cms.GlobalPagePermission_sites",
                        "cms.GlobalPagePermission",
                        "cms.PagePermission",
                        "cms.PageUser",
                        "cms.PageUserGroup",
                        "cms.Placeholder",
                        "cms.CMSPlugin",
                        "cms.Title",
                        "cms.PlaceholderReference",
                        "cms.StaticPlaceholder",
                        "cms.AliasPluginModel",
                        "cms.UrlconfRevision"
                    ]
                }
            ],
            [
                "menus",
                {
                    "comments": "django CMS menus system",
                    "natural_foreign": True,
                    "models": [
                        "menus.CacheKey"
                    ]
                }
            ],
            [
                "djangocms_picture",
                {
                    "comments": "Djangocms_Picture",
                    "natural_foreign": True,
                    "models": [
                        "djangocms_picture.Picture"
                    ]
                }
            ],
            [
                "djangocms_snippet",
                {
                    "comments": "Snippets",
                    "natural_foreign": True,
                    "models": [
                        "djangocms_snippet.Snippet",
                        "djangocms_snippet.SnippetPtr"
                    ]
                }
            ],
            [
                "djangocms_text_ckeditor",
                {
                    "comments": "django CMS Text CKEditor",
                    "natural_foreign": True,
                    "models": [
                        "djangocms_text_ckeditor.Text"
                    ]
                }
            ],
            # All CMS plugin configs must comes after DjangoCMS else the dump will be
            # broken for loading
            [
                "fobi.contrib.apps.djangocms_integration",
                {
                    "comments": "Fobi_Contrib_Apps_Djangocms_Integration",
                    "natural_foreign": True,
                    "models": [
                        "fobi_contrib_apps_djangocms_integration.FobiFormWidget"
                    ]
                }
            ],
        ]
