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
            return urlpatterns + i18n_patterns(
                path("", include("cms.urls")),
            )
        else:
            return urlpatterns + [
                path("", include("cms.urls")),
            ]
