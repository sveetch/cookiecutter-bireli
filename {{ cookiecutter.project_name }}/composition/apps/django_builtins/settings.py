"""
==========================
Django components settings
==========================

This module regroup only the builtin Django components classes.

"""
from pathlib import Path

from configurations import values

from project_composer.marker import EnabledApplicationMarker


def gettext(s):
    """
    A dummy function just to surround some string required to be translated, Django
    and gettext recognize it as a valid mark to discover translatable strings.
    """
    return s


class DjangoPaths(EnabledApplicationMarker):
    """
    Settings for essential path object related to the project structure.

    It should allways be in the first component classes to be executed since almost all
    component classes may rely on it directly or not.
    """
    # Root of project repository
    BASE_DIR = Path(__file__).parents[3]

    # Django project
    PROJECT_PATH = BASE_DIR / "project"

    # Variable content directory, mostly use for local db and media storage in
    # deployed environments
    VAR_PATH = BASE_DIR / "var"


class DjangoBase(EnabledApplicationMarker):
    """
    Base Django settings.

    This is the first executed classes so don't expect to rely on other
    settings here with setup method, all the settings need to be independant.

    This is for the common settings that are simple enough to not require their own
    classes.

    Opposed to the general structuring way, ``MIDDLEWARE`` and ``INSTALLED_APPS`` are
    defined here with all the common components you may expect from a barebone Django,
    this ensure a strong stability for all Django builtins and application classes.

    Application classes and environment classes still needs to alter these two settings
    in their own classes, not here.
    """
    # Debug mode is disabled by default to avoid security issues from an oversight
    DEBUG = values.BooleanValue(
        False,
        environ_name="DEBUG",
    )

    # Default Site object
    SITE_ID = values.PositiveIntegerValue(
        1,
        environ_name="SITE_ID",
    )

    # Dummy key, you need to fill a real secret key in your deployed environments
    SECRET_KEY = values.Value(
        "***TOPSECRET***",
        environ_name="SECRET_KEY",
    )

    # Https is always enabled on default
    HTTPS_ENABLED = True

    ADMINS = (
        # ("Admin", "PUT_ADMIN_EMAIL_HERE"),
    )

    MANAGERS = ADMINS

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    ALLOWED_HOSTS = ["*"]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "project.urls"

    # Python dotted path to the WSGI application used by Django"s runserver.
    WSGI_APPLICATION = "project.wsgi.application"

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        "django.forms",
    ]

    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"

    # To silent warning about application "AppConfig" which does not set
    # 'default_auto_field'
    DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

    @property
    def ENVIRONMENT(self):
        """
        Environment name in which the application is launched.
        """
        return self.__class__.__name__.lower()


class DjangoDatabase(EnabledApplicationMarker):
    """
    The database settings.
    """
    MIGRATION_MODULES = {}

    @classmethod
    def setup(cls):
        super().setup()

        # Every item for default db from DATABASES can be edited from environment
        # variables
        cls.DATABASES = {
            "default": {
                "ENGINE": values.Value(
                    "django.db.backends.sqlite3",
                    environ_name="DB_ENGINE",
                    environ_prefix=None,
                ),
                "NAME": values.Value(
                    cls.VAR_PATH / "db" / "db.sqlite3", environ_name="DB_NAME",
                    environ_prefix=None
                ),
                "USER": values.Value(None, environ_name="DB_USER", environ_prefix=None),
                "PASSWORD": values.Value(
                    None, environ_name="DB_PASSWORD", environ_prefix=None
                ),
                "HOST": values.Value(None, environ_name="DB_HOST", environ_prefix=None),
                "PORT": values.PositiveIntegerValue(
                    None, environ_name="DB_PORT", environ_prefix=None
                ),
            }
        }


class DjangoLanguage(EnabledApplicationMarker):
    """
    Everything related to I18N, I10N and Timezone.
    """
    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    TIME_ZONE = values.Value(
        "America/Chicago",
        environ_name="TIME_ZONE",
    )
    # TIME_ZONE = 'Europe/Paris' # French timezone

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = values.Value(
        "en",
        environ_name="LANGUAGE_CODE",
    )

    LANGUAGES = (
        ("en", gettext("English")),
        # ("de", gettext("Deutsch")),
        # ("es", gettext("Español")),
        # ("fr", gettext("French")),
        # ("it", gettext("Italiano")),
        # ("ja", gettext("日本語")),
        # ('zh', gettext('官话')),
    )

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = values.BooleanValue(
        True,
        environ_name="USE_I18N",
    )

    # Not a real Django settings, just a marker for other applications that implement
    # i18n urls to know if they can use it or not. For all that, applications may not
    # necessarily use it
    ENABLE_I18N_URLS = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    # DEPRECATED
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    # DEPRECATED
    USE_TZ = True

    @classmethod
    def setup(cls):
        super().setup()

        # A tuple of directories where Django looks for translation files
        cls.LOCALE_PATHS = [
            cls.PROJECT_PATH / "locale",
        ]


class DjangoStaticMedia(EnabledApplicationMarker):
    """
    Settings related to static files and media files.
    """
    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = "/media/"

    # URL prefix for static files.
    # Example: "http://example.com/static/", "http://static.example.com/"
    STATIC_URL = "/static/"

    @classmethod
    def setup(cls):
        super().setup()

        # Absolute filesystem path to the directory that will hold user-uploaded files.
        # Example: "/var/www/example.com/media/"
        cls.MEDIA_ROOT = cls.VAR_PATH / "media"

        # Absolute path to the directory static files should be collected to.
        # Don"t put anything in this directory yourself; store your static files
        # in apps "static/" subdirectories and in STATICFILES_DIRS.
        # Example: "/var/www/example.com/static/"
        cls.STATIC_ROOT = cls.VAR_PATH / "static"

        # Additional locations of static files
        cls.STATICFILES_DIRS = [
            # Put strings here, like "/home/html/static" or "C:/www/django/static".
            # Always use forward slashes, even on Windows.
            # Don"t forget to use absolute paths, not relative paths.
            cls.PROJECT_PATH / "static-sources",
        ]


class DjangoTemplate(EnabledApplicationMarker):
    """
    Settings for Django template engine.
    """
    # Ensure we can override applications widgets templates from project template
    # directory, require also "django.forms" in INSTALLED_APPS
    FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

    @classmethod
    def setup(cls):
        super().setup()

        cls.TEMPLATES = [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [
                    cls.PROJECT_PATH / "templates",
                ],
                "APP_DIRS": True,
                "OPTIONS": {
                    "debug": False,
                    "context_processors": [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.request",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                        # Basic processor to insert some common global variables
                        "project_utils.context_processors.site_metas",
                    ],
                },
            },
        ]
