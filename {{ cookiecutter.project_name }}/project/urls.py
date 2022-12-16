"""
==============================
Base Project URL configuration
==============================

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from project_composer.contrib.django.collector import ApplicationUrlCollector
from project_composer.contrib.django.helpers import project_urls

from project import _composer


# The very base of urls for the very basic stuff
urlpatterns = [
    path("admin/", admin.site.urls),
]


# Mount collected applications urls
urlpatterns += project_urls(_composer, settings, base_classes=[ApplicationUrlCollector])


# Finally the common static/media routes for development server
if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
