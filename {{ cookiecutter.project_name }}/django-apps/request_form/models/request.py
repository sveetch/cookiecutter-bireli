from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from phonenumber_field.modelfields import PhoneNumberField

from ..choices import get_subject_default, get_subject_choices


class RequestModel(models.Model):
    """
    Object to store request data from a submitted and validated form.
    """
    first_name = models.CharField(
        _("First name"), blank=False, null=False, max_length=100
    )
    last_name = models.CharField(
        _("Last name"), blank=False, null=False, max_length=100
    )
    profession = models.CharField(
        _("Profession"),
        blank=True,
        default="",
        max_length=100,
    )
    subject = models.CharField(
        _("Subject"),
        blank=True,
        max_length=55,
        choices=get_subject_choices(),
        default=get_subject_default(),
    )
    phone = PhoneNumberField(_("Phone"), null=True, blank=True)
    email = models.EmailField(_("E-mail"), blank=False, null=False)
    message = models.TextField(_("Message"), blank=False, null=False)
    data_confidentiality_policy = models.BooleanField(
        _("Data confidentiality policy"), blank=False, null=False
    )
    ip_address = models.GenericIPAddressField(blank=False, null=False)
    created_at = models.DateTimeField(_("Creation"), auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("request")
        verbose_name_plural = _("requests")

    def __str__(self):
        return "[{email}] - {subject}".format(
            email=self.email,
            subject=self.get_subject_display()
        )

    @property
    def full_name(self):
        return "{last_name} {first_name}".format(
            last_name=self.last_name,
            first_name=self.first_name,
        )


class RequestPluginModel(CMSPlugin):
    """
    Plugin model.

    This is a very basic model since it has no defined fields except placeholder slot
    relation implied by ``CMSPlugin`` inheritance.
    """

    def __str__(self):
        return _("Form include #{}").format(self.id)
