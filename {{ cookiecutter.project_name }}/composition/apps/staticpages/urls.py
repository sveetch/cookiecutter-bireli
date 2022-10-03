from django.urls import path, include

from staticpages.loader import StaticpagesLoader

from composer import EnabledComposableApplication


class StaticpageUrls(EnabledComposableApplication):
    """
    Staticpage application URLs mounter
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return urlpatterns + StaticpagesLoader().build_urls()
