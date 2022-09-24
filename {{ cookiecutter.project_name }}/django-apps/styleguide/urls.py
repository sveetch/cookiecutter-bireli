from django.urls import path

from .views import StyleguideIndexView


urlpatterns = [path("", StyleguideIndexView.as_view(), name="index")]
