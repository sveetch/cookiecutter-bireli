from staticpages.loader import StaticpagesLoader

from project_composer.marker import EnabledApplicationMarker


class StaticpageUrls(EnabledApplicationMarker):
    """
    Staticpage application URLs mounter
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return StaticpagesLoader().build_urls() + urlpatterns
