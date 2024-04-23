from django.urls import path

from .views import ExposedProjectGlobalsView


app_name = "project_utils"


urlpatterns = [
    path(
        "project-globals/",
        ExposedProjectGlobalsView.as_view(),
        name="project-globals"
    ),
]
