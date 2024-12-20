"""
This module regroups the builtin Django components classes.

Order of classes does matter.
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
    Settings for essential path objects related to the project structure.

    It should allways be in the first component classes to be executed since almost all
    component classes may rely on it directly or not.
    """
    # Root of project repository
    BASE_DIR = Path(__file__).parents[2]

    # Django project
    PROJECT_PATH = BASE_DIR / "project"

    # Variable content directory, mostly use for local db and media storage in
    # deployed environments
    VAR_PATH = BASE_DIR / "var"

    # Directory dedicated to hold various generated content from tools, opposed to the
    # var directory this one should be ensured to exists in deployed backend
    PARTS_PATH = BASE_DIR / "parts"

    # Set the Dotenv file path only if it exists
    _dotenv_path = BASE_DIR / ".env"
    if _dotenv_path.exists():
        DOTENV = _dotenv_path


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
    DEBUG = values.BooleanValue(False)

    # Default Site object
    SITE_ID = values.PositiveIntegerValue(1)

    # Dummy key, you need to fill a real secret key in your deployed environments
    SECRET_KEY = values.Value("***TOPSECRET***")

    # Https is always enabled on default
    HTTPS_ENABLED = values.BooleanValue(True)

    # Admin (name, email) for Django notifications
    ADMINS = values.SingleNestedTupleValue(
        (),
        seq_separator=";",
        separator=", ",
        environ_name="ADMINS"
    )

    MANAGERS = ADMINS

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    ALLOWED_HOSTS = values.ListValue(["*"], separator=",",
                                     environ_name="ALLOWED_HOSTS")

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        {% if cookiecutter.multiple_languages|lower != 'true' %}# {% endif %}"django.middleware.locale.LocaleMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django.contrib.sites.middleware.CurrentSiteMiddleware",
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

    # This may be overrided from custom authentication system like "Two factor"
    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"

    # To silent warning about application "AppConfig" which does not set
    # 'default_auto_field'
    DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

    # Django system check to disable
    SILENCED_SYSTEM_CHECKS = values.ListValue(
        [],
        separator=",",
        environ_name="SILENCED_SYSTEM_CHECKS"
    )

    # SMTP configuration
    EMAIL_BACKEND = values.Value("django.core.mail.backends.smtp.EmailBackend",
                                 environ_name="EMAIL_BACKEND")
    EMAIL_HOST = values.Value(None, environ_name="EMAIL_HOST")
    EMAIL_PORT = values.PositiveIntegerValue(None, environ_name="EMAIL_PORT")

    # Default email sender for various applications
    DEFAULT_FROM_EMAIL = values.Value(
        "no-reply@emencia.com",
        environ_name="DEFAULT_FROM_EMAIL",
    )

    # Default email recipient for applications that need it
    DEFAULT_TO_EMAIL = values.Value(
        "contact@emencia.com",
        environ_name="DEFAULT_TO_EMAIL",
    )

    # Enable strong password validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": (
                "django.contrib.auth.password_validation."
                "UserAttributeSimilarityValidator"
            ),
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # A set of some settings that are turned on in production settings
    SESSION_COOKIE_SECURE = False
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False
    CSRF_COOKIE_SECURE = False

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
        super(DjangoDatabase, cls).setup()

        # Every item for default db from DATABASES can be edited from environment
        # variables
        cls.DATABASES = {
            "default": {
                "ENGINE": values.Value(
                    "django.db.backends.sqlite3",
                    environ_name="DB_ENGINE",
                ),
                "NAME": values.Value(
                    cls.VAR_PATH / "db" / "db.sqlite3",
                    environ_name="DB_NAME",
                ),
                "USER": values.Value(
                    None,
                    environ_name="DB_USER",
                ),
                "PASSWORD": values.Value(
                    None,
                    environ_name="DB_PASSWORD",
                ),
                "HOST": values.Value(
                    None,
                    environ_name="DB_HOST",
                ),
                "PORT": values.PositiveIntegerValue(
                    None,
                    environ_name="DB_PORT",
                ),
                "OPTIONS": {},
            }
        }

        # Additional options
        db_sslmode_var = values.Value(
            None,
            environ_name="DJANGO_DB_SSLMODE",
            environ_prefix=None
        )
        if db_sslmode_var:
            cls.DATABASES["default"]["OPTIONS"]["sslmode"] = db_sslmode_var


class DjangoLanguage(EnabledApplicationMarker):
    """
    Everything related to I18N, I10N and Timezone.
    """
    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    TIME_ZONE = values.Value(
        "{{ cookiecutter._languages[cookiecutter.language].timezone }}",
        environ_name="TIME_ZONE",
    )

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = values.Value(
        "{{ cookiecutter.language }}",
        environ_name="LANGUAGE_CODE",
    )

    LANGUAGES = (
        {%- for key, value in cookiecutter._languages|dictsort %}
        {% if cookiecutter.multiple_languages|lower != 'true' and cookiecutter.language != key %}# {% endif %}("{{ key }}", "{{ value.name }}"),
        {%- endfor %}
    )

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = values.BooleanValue(
        True,
        environ_name="USE_I18N",
    )

    # Not a real Django builtin, just a common marker for other applications that needs
    # to know if i18n urls have to be used or not. Applications may not necessarily use
    # it, actually this is only used in some ``urls.py``
    ENABLE_I18N_URLS = {% if cookiecutter.multiple_languages|lower == 'true' %}True{% else %}False{% endif %}

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    # DEPRECATED
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    # DEPRECATED
    USE_TZ = True

    @classmethod
    def setup(cls):
        super(DjangoLanguage, cls).setup()

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
        super(DjangoStaticMedia, cls).setup()

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
        super(DjangoTemplate, cls).setup()

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
                    ],
                },
            },
        ]
