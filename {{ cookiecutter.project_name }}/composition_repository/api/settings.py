from project_composer.marker import EnabledApplicationMarker


class ApiSettings(EnabledApplicationMarker):
    """
    Project API settings
    """

    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            # Use Django"s standard 'django.contrib.auth' permissions,
            # or allow read-only access for unauthenticated users.
            "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
            # Only Django"s standard 'django.contrib.auth' permissions, every
            # authenticated user can read and anonymous are never allowed
            # "rest_framework.permissions.DjangoModelPermissions",
        ],
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        "PAGE_SIZE": 20,
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    }

    SPECTACULAR_SETTINGS = {
        "TITLE": "Your Project API",
        "DESCRIPTION": "Your project description",
        "VERSION": "1.0.0",
        "SERVE_INCLUDE_SCHEMA": False,
        "SWAGGER_UI_DIST": "SIDECAR",
        "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
        "REDOC_DIST": "SIDECAR",
    }

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend([
            "rest_framework",
            "drf_spectacular",
            "drf_spectacular_sidecar",
            "project_api",
        ])
