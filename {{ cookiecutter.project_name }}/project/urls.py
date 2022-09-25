"""
==============================
Base Project URL configuration
==============================


"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView

from staticpages.loader import StaticpagesLoader


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        TemplateView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "styleguide/",
        include(("styleguide.urls", "styleguide"), namespace="styleguide"),
    ),
]

staticpages_loader = StaticpagesLoader()
urlpatterns = staticpages_loader.build_urls() + urlpatterns

# This is only needed when using runserver with settings "DEBUG" enabled
if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
