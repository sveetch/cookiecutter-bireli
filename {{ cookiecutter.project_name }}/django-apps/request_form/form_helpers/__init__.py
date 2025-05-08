from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RequestDefaultFormHelper(FormHelper):
    """
    Default Crispy form layout.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attrs = {"novalidate": ""}
        self.form_action = reverse("request_form:request-form")
        self.form_class = "needs-validation"
        self.form_id = "request-form"
        self.form_tag = True

        self.add_input(
            Submit(
                "request-form-submit",
                _("Submit"),
                css_id="id_request-form-submit"
            )
        )
