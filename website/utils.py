from moviepy.editor import VideoFileClip
from django.http import FileResponse
from django.db import transaction
from django.conf import settings

from pathlib import Path
import os

from .models import Video


class AudioExtractor:
    def __init__(self: any, path_video: str) -> None:
        self.path_video = path_video
        self.video = VideoFileClip(self.path_video)

    @property
    def audio_file_path(self: any) -> str:
        """This property returns the path of the audio file"""

        return f"{settings.MEDIA_ROOT}/audios/{Path(self.path_video).stem}.mp3"

    def extract_audio_from_video(self: any) -> None:
        """This method extracts the audio from the video file."""

        self.video.audio.write_audiofile(self.audio_file_path)

        os.remove(self.path_video)

def download_audio_view(request, pk):
    # Get the video object
    video = Video.objects.get(pk=pk)

    # Create the response object
    response = FileResponse(video.audio_file, as_attachment=True)

    # Delete the file after sending the response
    response["X-Sendfile"] = video.audio_file.path

    # Delete the file from the file system
    if os.path.isfile(video.audio_file.path):
        os.remove(video.audio_file.path)

    # Delete the database record
    with transaction.atomic():
        video.delete()

    return response
