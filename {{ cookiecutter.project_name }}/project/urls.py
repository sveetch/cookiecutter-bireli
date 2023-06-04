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
from django.views.generic import TemplateView

from project_composer.contrib.django.collector import ApplicationUrlCollector
from project_composer.contrib.django.helpers import project_urls

from project import _composer


# The very base of urls for the very basic stuff
urlpatterns = [
    path("admin/", admin.site.urls),
]


# Views to debug some HTTP error templates
if settings.DEBUG:
    urlpatterns.extend([
        path("500/", TemplateView.as_view(template_name="500.html")),
        path("404/", TemplateView.as_view(template_name="404.html")),
        path("403/", TemplateView.as_view(template_name="403.html")),
    ])


# Mount collected applications urls
urlpatterns += project_urls(_composer, settings, base_classes=[ApplicationUrlCollector])


# Finally the common static/media routes for development server
if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
