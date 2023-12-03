from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


class SitemapsUrls(EnabledApplicationMarker):
    """
    Sitemaps urls
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return [
            path("", include("project_sitemaps.urls")),
        ] + urlpatterns
