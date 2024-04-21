from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


class ProjectUtilsUrls(EnabledApplicationMarker):
    """
    Project utils urls
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return [
            path("utils/", include("project_utils.urls")),
        ] + urlpatterns
