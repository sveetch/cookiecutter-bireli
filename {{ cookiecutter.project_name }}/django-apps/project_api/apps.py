from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProjectApiConfig(AppConfig):
    name = "project_api"
    verbose_name = _("Project API")
    default_auto_field = "django.db.models.AutoField"
