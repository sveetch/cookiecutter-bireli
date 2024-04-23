import json

from django.views.generic.base import TemplateView
from django.http import HttpResponseForbidden

from project_utils.context_processors import project_globals


class ExposedProjectGlobalsView(TemplateView):
    """
    A view to expose project global variables as enabled from context processor
    ``project_utils.context_processors.project_globals``.

    This view should never be exposed publicly there the view will respond with a
    basic Http 403 error.
    """
    template_name = "project_utils/project_globals.html"

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
        data = project_globals(self.request)

        return super().get_context_data(**{
            "project_globals_json": json.dumps(data, indent=4),
            "project_globals_variables": self.explore_dict(data),
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
