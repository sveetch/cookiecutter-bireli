import json

from django.views.generic.base import TemplateView
from django.http import HttpResponseForbidden

from project_utils.context_processors import site_metas


class ExposedSiteMetasView(TemplateView):
    """
    A view to expose site metas from context processor
    ``project_utils.context_processors.site_metas``.

    This view should never be exposed publicly there the view will respond with a
    basic Http 403 error.
    """
    template_name = "project_utils/site_metas.html"

    def explore_dict(self, data, variables=None, parents=None):
        """
        Explore meta dictionnary to compute the variable name path for values that are
        not dictionnary.

        .. Warning:
            It may have performance issue with huge deep dictionnary.
        """
        variables = variables or []
        parents = parents or []

        for k, v in data.items():
            parenting = parents + [k]
            if isinstance(v, dict):
                variables.extend(
                    self.explore_dict(v, parents=parenting)
                )
            else:
                variables.append(
                    (".".join(parenting), str(v))
                )

        return variables

    def get_context_data(self, **kwargs):
        data = site_metas(self.request)

        return super().get_context_data(**{
            "site_metas": json.dumps(data, indent=4),
            "site_variables": self.explore_dict(data),
        })

    def get(self, *args, **kwargs):
        """
        Check user is staff else return an error.
        """
        if (
            not self.request.user or
            (self.request.user and not self.request.user.is_staff)
        ):
            return HttpResponseForbidden("This view is reserved to staff only.")

        return super().get(*args, **kwargs)
