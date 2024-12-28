from django.contrib import admin
from django.template.defaultfilters import truncatechars

from ..models import RequestModel


@admin.register(RequestModel)
class RequestAdmin(admin.ModelAdmin):
    """
    Request form model representation for Django admin interface.
    """
    list_display = (
        "created_at",
        "subject",
        "display_full_name",
        "email",
        "ip_address",
    )
    ordering = RequestModel._meta.ordering
    search_fields = ["message", "email", "phone", "ip_address"]
    date_hierarchy = "created_at"
    list_filter = ("created_at", "subject")
    readonly_fields = ["created_at", "ip_address"]

    @admin.display(description="Extrait")
    def short_message(self, obj):
        return truncatechars(obj.message, 70)

    @admin.display(description="Nom complet")
    def display_full_name(self, obj):
        return obj.full_name
