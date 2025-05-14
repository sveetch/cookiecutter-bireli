from django.urls import path, include

from project_composer.marker import EnabledApplicationMarker


class CkeditorUrls(EnabledApplicationMarker):
    """
    django-ckeditor application URLs mounter
    """
    def load_urlpatterns(self, urlpatterns):
        """
        Mount application urls
        """
        urlpatterns = super().load_urlpatterns(urlpatterns)

        return [
            path(
                "ckeditor/",
                include("ckeditor_uploader.urls"),
            ),
        ] + urlpatterns
