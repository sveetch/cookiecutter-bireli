from django.urls import path

from .views import RequestFormView, RequestSuccessView

app_name = "request_form"


urlpatterns = [
    path("", RequestFormView.as_view(), name="request-form"),
    path("success/", RequestSuccessView.as_view(), name="request-success"),
]
