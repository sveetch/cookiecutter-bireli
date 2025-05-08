import logging
from smtplib import SMTPException

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
from django.forms import ModelForm
from django.template.loader import render_to_string
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from ..choices import get_subject_choices
from ..models import RequestModel
from ..form_helpers import RequestDefaultFormHelper
from ..utils.parsers import text_has_cyrillic_characters

logger = logging.getLogger(__name__)

USER_ERROR = _("An error occurred while sending the email. Please try again later.")

LOG_ERROR = _("Request form mail sending failed")


class RequestForm(ModelForm):
    """
    Request form save data from valid submit and possibly send email.

    Form layout is managed through a Crispy form class helper, a basic one is used as
    default but you can define a custom one from setting ``REQUEST_FORM_HELPER``.

    Since request object is not passed to a form and we need to know IP address, this
    form require the keyword argument ``request_ip_address`` fullfilled with a valid
    IP address syntax else the save will fail because of non null constraint on model
    field ``ip_address``.
    """
    captcha = (
        None
        if settings.REQUEST_FORM_DISABLE_CAPTCHA
        else ReCaptchaField(widget=ReCaptchaV3(action="requestform"))
    )
    data_confidentiality_policy = forms.BooleanField(
        required=True,
        error_messages={"required": _("You must accept data confidentiality policy.")},
    )

    class Meta:
        model = RequestModel
        fields = [
            "subject",
            "first_name",
            "last_name",
            "profession",
            "email",
            "phone",
            "message",
            "data_confidentiality_policy",
        ]

    def __init__(self, *args, **kwargs):
        self._request_ip_address = kwargs.pop("request_ip_address", None)

        super().__init__(*args, **kwargs)

        # Remove subject field from form when there is only the empty item
        if len(get_subject_choices()) < 2:
            del self.fields["subject"]

        # Optionally load helper module from given python path if any
        if settings.REQUEST_FORM_HELPER:
            self.helper = import_string(settings.REQUEST_FORM_HELPER)(self)
        # Else fallback to a default one
        else:
            self.helper = RequestDefaultFormHelper(self)

    def clean_email(self):
        """
        Check email against filters.
        """
        email = self.cleaned_data.get("email").lower()

        if email.endswith(settings.REQUEST_FORM_BANNED_TLD):
            raise forms.ValidationError(_("This email address isn't allowed."))

        return email

    def clean_message(self):
        """
        Check message against filters.
        """
        message = self.cleaned_data.get("message")

        if text_has_cyrillic_characters(message):
            raise forms.ValidationError(_("Cyrillic characters are not allowed."))

        return message

    def send_email(self, from_email, to, saved):
        """
        Email sending.
        """
        plain_body = render_to_string(
            "request_form/request/email.txt",
            {
                "first_name": saved.first_name,
                "last_name": saved.last_name,
                "phone": (
                    saved.phone.as_national
                    if saved.phone
                    else ""
                ),
                "email": saved.email,
                "message": saved.message,
                "profession": saved.profession,
                "subject": saved.get_subject_display(),
            }
        )

        email = EmailMessage(
            subject=settings.REQUEST_EMAIL_SUBJECT,
            body=plain_body,
            from_email=from_email,
            to=to,
        )

        try:
            email.send()
        except SMTPException as err_smtp:
            logger.error("{}: {}".format(LOG_ERROR, err_smtp))
            raise forms.ValidationError(USER_ERROR) from err_smtp
        except Exception as err:
            logger.error("{}: {}".format(LOG_ERROR, err))
            raise forms.ValidationError(USER_ERROR) from err

    def save(self, *args, **kwargs):
        """
        Save request object.

        Keyword Arguments:
            email_sending_enabled (boolean): If value is True it enables email sending
                else no email is sent. Defaut is ``True``.

                Email sending activation depends also from setting
                ``REQUEST_MAIL_DEFAULT_RECIPIENTS`` that must not be an empty value.
        """
        self.instance.ip_address = self._request_ip_address
        email_sending_enabled = kwargs.pop("email_sending_enabled", True)

        kwargs["commit"] = settings.REQUEST_SAVE_TO_DB
        request = super().save(*args, **kwargs)

        if settings.REQUEST_MAIL_DEFAULT_RECIPIENTS and email_sending_enabled:
            recipients = settings.REQUEST_MAIL_DEFAULT_RECIPIENTS
            if (
                settings.REQUEST_SUBJECTS and
                request.subject in settings.REQUEST_SUBJECTS and
                settings.REQUEST_SUBJECTS[request.subject].get("recipients")
            ):
                recipients = settings.REQUEST_SUBJECTS[request.subject]["recipients"]

            self.send_email(
                settings.REQUEST_FROM_EMAIL,
                recipients,
                request
            )

        return request
