from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SitemapsConfig(AppConfig):
    name = "project_sitemaps"
    verbose_name = _("Project sitemaps")
    default_auto_field = "django.db.models.AutoField"
