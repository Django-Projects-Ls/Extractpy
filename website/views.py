from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import FileResponse
from django.db import transaction

import os

from .models import Video
from .utils import VideoTranscriber


class SendVideoRequestHandler(CreateView):
    model = Video
    template_name = "home.html"
    fields = ["title", "video_file"]

    def form_valid(self, form):
        video = form.save()
        
        transcript = VideoTranscriber(video.video_file.path)
        transcript.extract_audio_from_video()

        video.audio_file = transcript.audio_file_path[transcript.audio_file_path.find("audios"):]
        video.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('download_audio', args=[str(self.object.id)])


def download_audio(request, pk):
    video = Video.objects.get(pk=pk)
    
    response = FileResponse(video.audio_file, as_attachment=True)

    # Delete the file after sending the response
    response['X-Sendfile'] = video.audio_file.path

    # Delete the file from the file system
    if os.path.isfile(video.audio_file.path):
        os.remove(video.audio_file.path)

    # Delete the video file as well
    if os.path.isfile(video.video_file.path):
        os.remove(video.video_file.path)

    # Delete the database record
    with transaction.atomic():
        video.delete()

    return response
