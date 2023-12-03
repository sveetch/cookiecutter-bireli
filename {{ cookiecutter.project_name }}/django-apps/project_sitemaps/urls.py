from django.contrib.sitemaps import views as sitemap_views
from django.urls import path

from cms.sitemaps import CMSSitemap
from lotus.sitemaps import ArticleSitemap


app_name = "project_sitemaps"


# Enabled sitemap classes with their section name
sitemap_classes = {
    "cms": CMSSitemap,
    "lotus-article": ArticleSitemap,
}


urlpatterns = [
    path(
        "sitemap.xml",
        sitemap_views.index,
        {
            "sitemap_url_name": "project_sitemaps:sitemap-section",
            "sitemaps": sitemap_classes,
        },
        name="sitemap-index"
    ),
    path(
        "sitemap-<section>.xml",
        sitemap_views.sitemap,
        {"sitemaps": sitemap_classes},
        name="sitemap-section"
    ),
]
