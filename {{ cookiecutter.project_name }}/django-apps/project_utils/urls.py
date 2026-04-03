from django.urls import path

from .views import ExposedProjectGlobalsView, StackInfoView


app_name = "project_utils"


urlpatterns = [
    path(
        "project-globals/",
        ExposedProjectGlobalsView.as_view(),
        name="project-globals"
    ),
    path(
        "stack-info/",
        StackInfoView.as_view(),
        name="stack-info"
    ),
]
