from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RequestDefaultFormHelper(FormHelper):
    """
    A crispy form class helper used as default form layout helper.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form_action = reverse("request_form:request-form")
        self.form_tag = True
        self.form_id = "request-form"

        self.add_input(
            Submit("save", _("Envoyer"), css_id="request-form-submit"),
        )
