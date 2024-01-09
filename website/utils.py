from moviepy.editor import VideoFileClip
from django.conf import settings

from pathlib import Path
from os import remove

class VideoTranscriber:
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
        
        remove(self.path_video)
