from django.urls import include, path

from project_composer.marker import EnabledApplicationMarker


class DjangoTwoFactorAuthUrls(EnabledApplicationMarker):
    """
    Django two factor authentication urls
    """

    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)
        from two_factor.urls import urlpatterns as tf_urls

        return [path("", include(tf_urls))] + urlpatterns
