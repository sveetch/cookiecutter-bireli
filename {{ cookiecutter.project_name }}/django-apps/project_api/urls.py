"""
API URLs
"""
from django.urls import path, include

from rest_framework import routers

from lotus.viewsets import ArticleViewSet, AuthorViewSet, CategoryViewSet
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)


app_name = "project-api"


# Lotus routes
router = routers.DefaultRouter()
router.register(r"lotus/article", ArticleViewSet, basename="article")
router.register(r"lotus/author", AuthorViewSet, basename="author")
router.register(r"lotus/category", CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),
    # Schema manifest in YAML
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # API browser interfaces (choose one, remove the other)
    # Note how these view need the final url name including namespace
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="project-api:schema"),
        name="swagger-ui"
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="project-api:schema"),
        name="redoc"
    ),
]
