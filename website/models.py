from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to="videos/")
    audio_file = models.FileField(upload_to="audios/", null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
