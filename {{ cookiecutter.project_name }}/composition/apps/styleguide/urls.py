from django.urls import path, include

from composer import EnabledComposableApplication


class StyleguideUrls(EnabledComposableApplication):
    """
    Styleguide application URLs mounter
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return urlpatterns + [
            path(
                "styleguide/",
                include(
                    ("styleguide.urls", "styleguide"),
                    namespace="styleguide"
                ),
            ),
        ]
