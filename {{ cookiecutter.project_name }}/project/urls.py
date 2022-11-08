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

from project_composer.collector import ApplicationUrlCollector

from project import _composer


# The very base of urls for the very basic stuff
urlpatterns = [
    path("admin/", admin.site.urls),
]


# Search for all enabled message classes
_classes = _composer.call_processor("DjangoUrlsProcessor", "export")

# Add the base messager as the base inheritance
_COMPOSED_CLASSES = _classes + [ApplicationUrlCollector]

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
