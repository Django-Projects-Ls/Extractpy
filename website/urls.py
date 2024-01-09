from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path("home", views.SendVideoRequestHandler.as_view(), name="home"),
    path("download/<int:pk>", views.download_audio, name="download_audio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
