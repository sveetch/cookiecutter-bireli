"""
====================
Django-fobi settings
====================

"""
from project_composer.marker import EnabledApplicationMarker


class FobiSettings(EnabledApplicationMarker):
    """
    django-fobi a form builder/generator
    """
    # Fobi admin theme, there is not bootstrap>3 theme so we start with this one
    FOBI_DEFAULT_THEME = "bootstrap3"

    # Bleach validation rules for allowed attributes in richtext plugin
    FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES = {
        "*": ["class"],
        "a": ["href", "title", "class"],
        "abbr": ["title"],
        "acronym": ["title"],
        "img": ["alt"],
    }

    # Bleach validation rules for allowed tags in richtext plugin
    FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS = [
        "a",
        "abbr",
        "acronym",
        "b",
        "blockquote",
        "code",
        "div",
        "em",
        "i",
        "li",
        "ol",
        "p",
        "small",
        "strong",
        "ul",
    ]

    @classmethod
    def setup(cls):
        super(FobiSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            # Core
            "fobi",

            # Enabled themes, the simple one is a required base theme
            "fobi.contrib.themes.bootstrap3",
            "fobi.contrib.themes.simple",

            # Enabled form fields
            "fobi.contrib.plugins.form_elements.fields.boolean",
            "fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple",
            "fobi.contrib.plugins.form_elements.fields.date",
            # fobi.contrib.plugins.form_elements.fields.date_drop_down",
            "fobi.contrib.plugins.form_elements.fields.datetime",
            # fobi.contrib.plugins.form_elements.fields.decimal",
            "fobi.contrib.plugins.form_elements.fields.email",
            # fobi.contrib.plugins.form_elements.fields.file",
            # fobi.contrib.plugins.form_elements.fields.float",
            # fobi.contrib.plugins.form_elements.fields.hidden",
            "fobi.contrib.plugins.form_elements.fields.input",
            "fobi.contrib.plugins.form_elements.fields.integer",
            # fobi.contrib.plugins.form_elements.fields.ip_address",
            # fobi.contrib.plugins.form_elements.fields.null_boolean",
            # fobi.contrib.plugins.form_elements.fields.password",
            "fobi.contrib.plugins.form_elements.fields.radio",
            # fobi.contrib.plugins.form_elements.fields.regex",
            "fobi.contrib.plugins.form_elements.fields.select",
            # fobi.contrib.plugins.form_elements.fields.select_model_object",
            "fobi.contrib.plugins.form_elements.fields.select_multiple",
            # fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects",
            # fobi.contrib.plugins.form_elements.fields.slug",
            "fobi.contrib.plugins.form_elements.fields.text",
            "fobi.contrib.plugins.form_elements.fields.textarea",
            "fobi.contrib.plugins.form_elements.fields.time",
            "fobi.contrib.plugins.form_elements.fields.url",

            # Enabled form content
            "fobi.contrib.plugins.form_elements.security.recaptcha",
            # fobi.contrib.plugins.form_elements.content.content_image",
            # fobi.contrib.plugins.form_elements.content.content_image_url",
            # fobi.contrib.plugins.form_elements.content.content_text",
            "fobi.contrib.plugins.form_elements.content.content_richtext",

            # Form inclusion as a CMS plugin
            "fobi.contrib.apps.djangocms_integration",

            # Enabled form handlers
            "fobi.contrib.plugins.form_handlers.db_store",
            # fobi.contrib.plugins.form_handlers.http_repost",
            "fobi.contrib.plugins.form_handlers.mail",
            "fobi.contrib.plugins.form_handlers.mail_sender",
        ])

        # Required by content_image even if disabled it may trouble model fixture
        # dump
        if "easy_thumbnails" not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.extend([
                "easy_thumbnails"
            ])

        # Basic processor to insert some common global variables
        cls.TEMPLATES[0]["OPTIONS"]["context_processors"].extend([
            "fobi.context_processors.theme",
        ])

        # Plug the captcha component to the recaptcha keys
        cls.FOBI_PLUGIN_INVISIBLE_RECAPTCHA_SITE_KEY = cls.RECAPTCHA_PUBLIC_KEY
        cls.FOBI_PLUGIN_INVISIBLE_RECAPTCHA_SITE_SECRET = cls.RECAPTCHA_PRIVATE_KEY
