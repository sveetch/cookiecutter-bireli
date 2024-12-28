from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase

from request_form.models import RequestPluginModel
from request_form.forms import RequestForm


class RequestPlugin(CMSPluginBase):
    """
    Request form plugin.

    This is a simple plugin without any option and will includes the form in an initial
    state.

    Obviously, the CMS page where it is included can not manage POST request so the
    form will redirect any request to an URL from the request application itself.
    """

    module = _("request-form")
    name = _("Request form")
    model = RequestPluginModel
    render_template = "request_form/request/plugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        context.update({
            "request_form": RequestForm(),
        })

        return context
