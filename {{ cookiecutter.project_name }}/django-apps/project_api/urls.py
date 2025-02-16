"""
API URLs
"""
from django.urls import path, include

from rest_framework import routers

from lotus.viewsets import ArticleViewSet, AuthorViewSet, CategoryViewSet


app_name = "project-api"


# Lotus routes
router = routers.DefaultRouter()
router.register(r"lotus/article", ArticleViewSet, basename="article")
router.register(r"lotus/author", AuthorViewSet, basename="author")
router.register(r"lotus/category", CategoryViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),
]
