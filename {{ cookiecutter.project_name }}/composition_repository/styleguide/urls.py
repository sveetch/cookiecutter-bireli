from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


class StyleguideUrls(EnabledApplicationMarker):
    """
    Styleguide application URLs mounter
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return [
            path(
                "styleguide/",
                include(
                    ("styleguide.urls", "styleguide"),
                    namespace="styleguide"
                ),
            ),
        ] + urlpatterns
