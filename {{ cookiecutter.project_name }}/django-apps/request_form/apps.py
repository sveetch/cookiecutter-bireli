from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RequestConfig(AppConfig):
    name = "request_form"
    verbose_name = _("Request form")
    default_auto_field = "django.db.models.AutoField"
