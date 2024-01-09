from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import FileResponse
from django.db import transaction

import os

from .utils import AudioExtractor
from .models import Video
from .forms import VideoForm


class SendVideoRequestHandler(CreateView):
    model = Video
    template_name = "upload.html"
    form_class = VideoForm

    def form_valid(self, form):
        # Save the video object
        video = form.save()

        # Extract the audio from the video
        extractor = AudioExtractor(video.video_file.path)
        extractor.extract_audio_from_video()

        # Save the audio file path in the database
        video.audio_file = extractor.audio_file_path[
            extractor.audio_file_path.find("audios") :
        ]
        video.save()

        # Return the form_valid method of the parent class
        return super().form_valid(form)

    def get_success_url(self):
        # Return the URL of the download view
        return reverse_lazy("download_audio", args=[str(self.object.id)])


def download_audio(request, pk):
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
