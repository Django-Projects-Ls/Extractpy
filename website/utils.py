from moviepy.editor import VideoFileClip
from django.conf import settings
from openai import OpenAI

from pathlib import Path
from os import remove

class VideoTranscriber:
    def __init__(self: any, path_video: str) -> None:
        self.path_video = path_video
        self.video = VideoFileClip(self.path_video)
        self.client = OpenAI(api_key=settings.API_KEY)

    @property
    def audio_file_path(self: any) -> str:
        """This property returns the path of the audio file"""

        return f"{settings.MEDIA_ROOT}/audios/{Path(self.path_video).stem}.mp3"

    def extract_audio_from_video(self: any) -> None:
        """This method extracts the audio from the video file."""

        self.video.audio.write_audiofile(self.audio_file_path)

    def generate_transcript(self: any) -> str:
        """This method returns the transcript of the video file."""

        try:
            with open(self.audio_file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="txt",
                )
        finally:
            remove(self.path_video) # Remove the video file after generating the transcript
            remove(self.audio_file_path) # Remove the audio file after generating the transcript

        return transcript

    def generate_summary(self: any, text: str) -> str:
        """This method returns the summary of the video file."""

        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Summarize the following video: {text}",
        )

        return response.choices[0].text