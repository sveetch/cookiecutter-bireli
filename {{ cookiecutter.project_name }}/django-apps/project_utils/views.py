from fobi.views.class_based import PermissionMixin, DashboardView


class LoginRequiredDashboardView(DashboardView, PermissionMixin):
    """
    This is a temporary view to patch incorrect behavior from DashboardView which omits
    PermissionMixin inheritance and so is reachable from anonymous.

    It is until a new fobi release include the fix for:

    https://github.com/barseghyanartur/django-fobi/issues/300
    """
    pass
