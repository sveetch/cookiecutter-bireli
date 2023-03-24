from django.urls import path, re_path, include

from project_composer.marker import EnabledApplicationMarker

from project_utils.views import LoginRequiredDashboardView


class FobiUrls(EnabledApplicationMarker):
    """
    django-fobi application URLs mounter
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return [
            # View URLs
            path(
                "fobi/",
                include("fobi.urls.class_based.view")
            ),
            # TODO: Temporary overrides the dashboard to use patched view for login
            # required
            re_path(
                r"^fobi/$",
                view=LoginRequiredDashboardView.as_view(),
                name="fobi.dashboard",
            ),
            # Edit URLs
            path(
                "fobi/",
                include("fobi.urls.class_based.edit")
            ),
            # DB Store plugin URLs
            path(
                "fobi/plugins/form-handlers/db-store/",
                include("fobi.contrib.plugins.form_handlers.db_store.urls")
            ),
        ] + urlpatterns
