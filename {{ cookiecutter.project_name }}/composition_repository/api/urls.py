from django.urls import include, path

from project_composer.marker import EnabledApplicationMarker


class ApiUrls(EnabledApplicationMarker):
    """
    API urls
    """

    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return [
            path("api/", include("project_api.urls")),
        ] + urlpatterns
