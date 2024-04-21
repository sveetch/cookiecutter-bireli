from django.urls import path

from .views import ExposedSiteMetasView


app_name = "project_utils"


urlpatterns = [
    path("site-metas/", ExposedSiteMetasView.as_view(), name="site-metas"),
]
