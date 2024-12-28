from django.utils.translation import gettext_lazy as _

from configurations import values
from project_composer.marker import EnabledApplicationMarker


class RequestFormSettings(EnabledApplicationMarker):
    """
    RequestForm settings

    The form is able to work if setting ``REQUEST_SUBJECTS`` is
    empty, then so the mail will be sent to default recipient from setting
    ``REQUEST_MAIL_DEFAULT_RECIPIENTS``.
    """

    PHONENUMBER_DEFAULT_FORMAT = "NATIONAL"
    PHONENUMBER_DEFAULT_REGION = "FR"
    PHONENUMBER_DB_FORMAT = "NATIONAL"

    # If false, request form data are not saved in database when form succeed.
    REQUEST_SAVE_TO_DB = True

    # Crispy form layout class
    REQUEST_FORM_HELPER = "request_form.form_helpers.layouts.RequestFormDefaultLayout"

    # All emails that end with these extensions
    #  are not allowed to submit forms by email
    REQUEST_FORM_BANNED_TLD = values.Value(
        (".ru", "qq.com"),
        environ_name="REQUEST_FORM_BANNED_TLD",
    )

    REQUEST_EMAIL_SUBJECT = values.Value(
        _("Website request form"),
        environ_name="REQUEST_EMAIL_SUBJECT",
    )

    # Default email recipient when a subject choice is not matched from
    # 'REQUEST_SUBJECTS'. If this setting is setted to an empty value
    # no email will be sent even if it could have matched one from
    # ``REQUEST_SUBJECTS``
    REQUEST_MAIL_DEFAULT_RECIPIENTS = values.ListValue(
        ["contact+default@emencia.com"],
        separator=",",
        environ_name="REQUEST_MAIL_DEFAULT_RECIPIENTS"
    )

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend(["request_form", "phonenumber_field"])

        cls.REQUEST_FROM_EMAIL = values.Value(
            cls.DEFAULT_FROM_EMAIL,
            environ_name="REQUEST_FROM_EMAIL",
        )

        cls.REQUEST_TO_EMAIL = values.Value(
            cls.DEFAULT_TO_EMAIL,
            environ_name="REQUEST_TO_EMAIL",
        )

        cls.REQUEST_SUBJECTS = {
            # "ENTREPRISE": {
            #     "label": "Entreprise",
            #     "recipients": ["contact+entreprise@emencia.com"],
            # },
        }
