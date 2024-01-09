from django.db import models


# Create your models here.
class Video(models.Model):
    video_file = models.FileField(upload_to="videos/")
    audio_file = models.FileField(upload_to="audios/", null=True, blank=True)
