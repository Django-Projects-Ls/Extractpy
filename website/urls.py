from django.urls import path

from . import views

urlpatterns = [
    path("home", views.SendVideoRequestHandler.as_view(), name="home"),
]
