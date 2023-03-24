from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


class CmsBaseUrls(EnabledApplicationMarker):
    """
    CMS urls
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        if self.settings.ENABLE_I18N_URLS:
            return i18n_patterns(
                path("", include("cms.urls")),
            ) + urlpatterns
        else:
            return [
                path("", include("cms.urls")),
            ] + urlpatterns
