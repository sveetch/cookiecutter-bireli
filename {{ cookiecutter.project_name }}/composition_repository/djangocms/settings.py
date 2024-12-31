import copy

from project_composer.marker import EnabledApplicationMarker


class CmsBaseSettings(EnabledApplicationMarker):
    """
    DjangoCMS core and simple base plugins
    """
    # Mandatory
    CMS_CONFIRM_VERSION4 = True

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

    # Values to use for custom CMS sitemap options
    CMS_SITEMAP_DEFAULT_PRIORITY = 0.80
    CMS_SITEMAP_HOMEPAGE_PRIORITY = 1.0
    CMS_SITEMAP_CHANGEFREQ = "monthly"

    # Enable inline editing with djangocms-text
    # https://github.com/django-cms/djangocms-text#inline-editing-feature
    TEXT_INLINE_EDITING = False

    # Allow deletion of version objects
    DJANGOCMS_VERSIONING_ALLOW_DELETING_VERSIONS = True

    @classmethod
    def setup(cls):
        super(CmsBaseSettings, cls).setup()

        # Admin style needs to be before "django.contrib.admin" which we assume it's
        # always first in list
        cls.INSTALLED_APPS.insert(0, "djangocms_admin_style")

        # Then we push the common cms stack
        cls.INSTALLED_APPS.extend([
            "treebeard",
            "cms",
            "menus",
            "sekizai",
            "djangocms_alias",
            "djangocms_versioning",
            # "djangocms_picture",
            # "djangocms_snippet",
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


class CmsCkeditor4Settings(EnabledApplicationMarker):
    """
    CMS CKEditor4 plugin

    .. NOTE::
        CKEditor v4 is the legacy version we used everywhere but is unmaintained with
        security flaws. We plan to move to v5 as soon as possible.
    """
    @classmethod
    def setup(cls):
        super().setup()

        # Then we push the common cms stack
        cls.INSTALLED_APPS.extend([
            "djangocms_text",
            "djangocms_text.contrib.text_ckeditor4",
        ])

        cls.TEXT_EDITOR = "djangocms_text.contrib.text_ckeditor4.ckeditor4"

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
            "extraPlugins": "youtube,vimeo,codemirror",
            "removePlugins": "exportpdf,image,flash,stylesheetparser",
            "toolbar": "CMS",
            # The config for TextPlugin only
            "toolbar_CMS": [
                ["Undo", "Redo"],
                [
                    # "cmsplugins", "-",
                    "ShowBlocks"
                ],
                ["Format", "Styles"],
                ["RemoveFormat"],
                ["Maximize"],
                "/",
                ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["Link", "Unlink"],
                [
                    "Youtube", "Vimeo", "-", "NumberedList", "BulletedList",
                    "-", "Table", "-", "CreateDiv", "HorizontalRule",
                ],
                # ["Iframe"],
                # ["Templates"],
                ["Source"],
            ],
            # The config for plugins which use the editor widget from
            # djangocms-text-ckeditor
            "toolbar_HTMLField": [
                ["Undo", "Redo"],
                ["ShowBlocks"],
                ["Format", "Styles"],
                ["RemoveFormat"],
                ["Maximize"],
                "/",
                ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["Link", "Unlink"],
                [
                    "Youtube", "Vimeo", "-", "NumberedList", "BulletedList",
                    "-", "Table", "-", "CreateDiv", "HorizontalRule",
                ],
                # ["Iframe"],
                # ["Templates"],
                ["Source"],
            ],
        })


class CmsCkeditor5Settings:
    """
    CMS CKEditor5 plugin

    .. NOTE::
        Working but currently not enabled until we are ready to migrate from v4 to v5.

        Disable the ``CmsCkeditor4Settings`` settings class if you want are going this
        v5 settings class.
    """
    @classmethod
    def setup(cls):
        super().setup()

        # Then we push the common cms stack
        cls.INSTALLED_APPS.extend([
            "djangocms_text",
            "djangocms_text_ckeditor5",
        ])

        cls.TEXT_EDITOR = "djangocms_text_ckeditor5.ckeditor5"
