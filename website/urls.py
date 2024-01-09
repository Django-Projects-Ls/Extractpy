from django.urls import path

from . import views

urlpatterns = [
    path("upload", views.SendVideoRequestHandler.as_view(), name="upload_video"),
    path("download/<int:pk>", views.download_audio, name="download_audio"),
]
