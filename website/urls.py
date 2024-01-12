from django.urls import path

from . import views
from .utils import download_audio_view

urlpatterns = [
    path("", views.home_redirect_view, name="home_redirect"),
    path("upload", views.SendVideoRequestHandler.as_view(), name="upload_video"),
    path("download/<int:pk>", download_audio_view, name="download_audio"),
]
