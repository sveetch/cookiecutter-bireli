from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


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
