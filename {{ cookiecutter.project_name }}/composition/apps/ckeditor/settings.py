"""
========================
Django CKEditor settings
========================

"""
import copy

from project_composer.marker import EnabledApplicationMarker


class CkeditorSettings(EnabledApplicationMarker):
    """
    WYSIWYG HTML editor integration for Django
    """

    # This won't work with django-filer, only filebrowser
    # CKEDITOR_UPLOAD_PATH = "uploads/"

    # Base configuration shared for django-ckeditor and djangocms-text-ckeditor
    # Avoid to change it unless you are aware of incompatibilities between ckeditor
    # apps
    CKEDITOR_SHARED_CONF = {
        "language": "{% raw %}{{ language }}{% endraw %}",
        "skin": "moono-lisa",
        "toolbarCanCollapse": False,
        "contentsCss": "/static/css/ckeditor.css",
        # Enabled showblocks as default behavior
        "startupOutlineBlocks": True,
        # Enable some plugins
        "extraPlugins": "youtube,vimeo,codemirror",
        # Disable element filter to enable full HTML5, also this will let
        # append any code, even bad syntax and malicious code, so be careful
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        # Image plugin options
        "image_prefillDimensions": False,
        # Youtube plugin options
        "youtube_related": False,
        "youtube_responsive": True,
        "youtube_disabled_fields": [
            "chkOlderCode",
            "chkNoEmbed",
        ],
        # Vimeo plugin options
        "vimeo_responsive": True,
        # Justify text using CSS framework utility classes
        "justifyClasses": [
            "text-start",
            "text-center",
            "text-end",
        ],
        # Uncheck the checkbox that replace whole content with the selected
        # template (if any)
        "templates_replaceContent": False,
        # URL to reach Filebrowser browser screen
        "filebrowserBrowseUrl": "/admin/filebrowser/browse?pop=3",
        # URLs for Javascripts that define content templates
        "templates_files": [
            "/ckeditor/editor_site_templates.js"
        ],
    }

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend([
            "ckeditor",
        ])

        cls.CKEDITOR_CONFIGS = copy.deepcopy(cls.CKEDITOR_SHARED_CONF)

        # Default config for every CKeditor field that does not define a config name.
        # It just duplicate the shared config
        cls.CKEDITOR_CONFIGS["default"] = copy.deepcopy(cls.CKEDITOR_SHARED_CONF)
        cls.CKEDITOR_CONFIGS["default"].update({
            "width": "100%",
            "height": 400,
            "toolbar": "Default",
            "toolbar_Default": [
                ["Undo", "Redo"],
                ["ShowBlocks"],
                ["Format", "Styles"],
                ["RemoveFormat"],
                # Disable Maximize because currently cause issue with admin-styles
                # fixed header
                #["Maximize"],
                "/",
                ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["TextColor"],
                ["Link", "Unlink"],
                ["Image", "Youtube", "Vimeo", "-", "NumberedList", "BulletedList",
                    "-", "Table", "-", "CreateDiv", "HorizontalRule"],
                #["Iframe"],
                #["Templates"],
                ["Source"],
            ],
        })
