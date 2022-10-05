"""
==============================
Base Project URL configuration
==============================


"""
from pathlib import Path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from project_composer.collector import ApplicationUrlCollector
from project_composer.compose import ComposeDjangoUrls


# The very base of urls for the very basic stuff
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        TemplateView.as_view(template_name="index.html"),
        name="index",
    ),
]


# Compose urls from enabled applications
_composer = ComposeDjangoUrls(
    Path("./composition-manifest.json").resolve(),
    "composition.apps"
)


# Add the base django-configuration class as the base inheritance
_COMPOSED_CLASSES = _composer.export() + [ApplicationUrlCollector]


# Build Urls class from composed urls
ComposedProjectUrls = type(
    "ComposedProjectUrls",
    tuple(_COMPOSED_CLASSES),
    {}
)


# Mount collected applications urls
mounter = ComposedProjectUrls(settings)
urlpatterns = mounter.collect(urlpatterns)


# Finally the common static/media routes for development server
if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
