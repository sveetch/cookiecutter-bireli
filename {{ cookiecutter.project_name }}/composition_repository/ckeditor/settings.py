import copy

from project_composer.marker import EnabledApplicationMarker


class CkeditorSettings(EnabledApplicationMarker):
    """
    CKEditor, WYSIWYG HTML editor integration for Django
    """

    # Enable file upload with 'ckeditor_uploader'
    # CKEDITOR_UPLOAD_PATH = "uploads/"

    # Base configuration shared for django-ckeditor and djangocms-text-ckeditor
    # Avoid to change it unless you are aware of incompatibilities between ckeditor
    # apps
    CKEDITOR_SHARED_CONF = {
        "language": "{% raw %}{{ language }}{% endraw %}",
        "skin": "moono-lisa",
        "toolbarCanCollapse": False,
        # "contentsCss": "/static/css/ckeditor.css",
        # Enabled showblocks as default behavior
        "startupOutlineBlocks": True,
        # Enable some plugins
        "extraPlugins": "codemirror",
        # Disable element filter to enable full HTML5, also this will let
        # append any code, even bad syntax and malicious code, so be careful
        "removePlugins": "exportpdf,flash,stylesheetparser",
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
        # URLs for Javascripts that define content templates
        # "templates_files": [
        #     "/ckeditor/editor_site_templates.js"
        # ],
    }

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend([
            "ckeditor",
        ])

        cls.CKEDITOR_CONFIGS = copy.deepcopy(cls.CKEDITOR_SHARED_CONF)

        # Default minimal config for every CKeditor field that does not define a
        # config name. It just inherits the shared config.
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
                ["Maximize"],
                "/",
                ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["TextColor"],
                ["Link", "Unlink"],
                [
                    "NumberedList", "BulletedList", "-", "Table", "-", "CreateDiv",
                    "HorizontalRule",
                ],
                # ["Iframe"],
                # ["Templates"],
                ["Source"],
            ],
        })

        # Basic configuration for application using 'django-ckeditor', include common
        # extra plugins (and replace image plugin with image2 plugin)
        cls.CKEDITOR_CONFIGS["basic"] = copy.deepcopy(cls.CKEDITOR_SHARED_CONF)
        cls.CKEDITOR_CONFIGS["basic"].update({
            "width": "100%",
            "height": 400,
            "extraPlugins": "image2,youtube,vimeo,codemirror",
            "removePlugins": "exportpdf,image,flash,stylesheetparser",
            "toolbar": "basic",
            "toolbar_basic": [
                ["Undo", "Redo"],
                ["ShowBlocks"],
                ["Format", "Styles"],
                ["RemoveFormat"],
                ["Maximize"],
                "/",
                ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["TextColor"],
                ["Link", "Unlink"],
                [
                    "Image", "Youtube", "Vimeo", "-", "NumberedList", "BulletedList",
                    "-", "Table", "-", "CreateDiv", "HorizontalRule",
                ],
                # ["Iframe"],
                # ["Templates"],
                ["Source"],
            ],
        })
