from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from project_composer.marker import EnabledApplicationMarker


class LotusUrls(EnabledApplicationMarker):
    """
    Lotus urls
    """

    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls

        TODO:

        Lotus currently require to be mounted in 'i18n_patterns' since it require
        language code and stands on LocaleMiddleware only.
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return i18n_patterns(
            path("blog/", include("lotus.urls")),
        ) + urlpatterns
