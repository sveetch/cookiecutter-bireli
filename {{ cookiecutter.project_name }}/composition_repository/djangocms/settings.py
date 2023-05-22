import copy

from project_composer.marker import EnabledApplicationMarker


class CmsBaseSettings(EnabledApplicationMarker):
    """
    DjangoCMS core and simple base plugins
    """
    # Available page templates
    CMS_TEMPLATES = [
        ("pages/free.html", "Free HTML"),
        ("pages/single_column.html", "Single column"),
    ]

    # Required to enable iframes used by CMS admin modals
    X_FRAME_OPTIONS = "SAMEORIGIN"

    # Uncomment this to enable per-object user permission
    # See http://docs.django-cms.org/en/latest/topics/permissions.html
    # CMS_PERMISSION = True

    # Available CMS page templates for tests purposes only
    TEST_PAGE_TEMPLATES = {
        "test-basic": "tests/pages/basic.html",
    }

    @classmethod
    def setup(cls):
        super(CmsBaseSettings, cls).setup()

        # Admin style needs to be before "django.contrib.admin" which we assume it's
        # always first in list
        cls.INSTALLED_APPS.insert(0, "djangocms_admin_style")

        # Then we push the common cms stack
        cls.INSTALLED_APPS.extend([
            "cms",
            "menus",
            "treebeard",
            "sekizai",
            "djangocms_picture",
            "djangocms_snippet",
        ])

        # Add CMS machinary
        cls.MIDDLEWARE.extend([
            "cms.middleware.utils.ApphookReloadMiddleware",
            "cms.middleware.user.CurrentUserMiddleware",
            "cms.middleware.page.CurrentPageMiddleware",
            "cms.middleware.toolbar.ToolbarMiddleware",
            "cms.middleware.language.LanguageCookieMiddleware",
        ])

        cls.TEMPLATES[0]["OPTIONS"]["context_processors"].extend([
            "sekizai.context_processors.sekizai",
            "cms.context_processors.cms_settings",
        ])


class CmsCkeditorSettings(EnabledApplicationMarker):
    """
    CMS CKEditor plugin

    Although it has its own classes the CMS cannot work properly without it, so it's
    not an optional plugin.
    """
    @classmethod
    def setup(cls):
        super(CmsCkeditorSettings, cls).setup()

        # Then we push the common cms stack
        cls.INSTALLED_APPS.extend([
            "djangocms_text_ckeditor",
        ])

        # html5lib sanitizer parameters to allow some unsafe elements
        cls.TEXT_ADDITIONAL_TAGS = (
            "iframe",
        )

        cls.TEXT_ADDITIONAL_ATTRIBUTES = (
            # For internal awful hack to not have href links in html
            "allowfullscreen",
        )

        # Copy shared basic ckeditor configuration
        cls.CKEDITOR_SETTINGS = copy.deepcopy(cls.CKEDITOR_SHARED_CONF)

        # This is were you"ll put configuration for djangocms-text-ckeditor only
        cls.CKEDITOR_SETTINGS.update({
            "toolbar": "CMS",
            "toolbar_CMS": [
                ["Undo", "Redo"],
                # ["cmsplugins", "-", "ShowBlocks"],
                ["ShowBlocks"],
                ["Format", "Styles"],
                ["RemoveFormat"],
                ["Maximize"],
                "/",
                [
                    "Bold", "Italic", "Underline", "-",
                    "Subscript", "Superscript"
                ],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["Link", "Unlink"],
                [
                    'Image', 'Youtube', 'Vimeo', '-',
                    'NumberedList', 'BulletedList', "-",
                    "Table", "-",
                    "CreateDiv", "HorizontalRule",
                ],
                # ["Iframe"],
                # ["Templates"],
                ["Source"],
            ],
        })

        # Share the same config for djangocms_text_ckeditor field and derived
        # CKEditor widgets/fields from plugins
        cls.CKEDITOR_SETTINGS["toolbar_HTMLField"] = (
            cls.CKEDITOR_SETTINGS["toolbar_CMS"]
        )
