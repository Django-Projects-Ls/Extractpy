from django.views.generic.edit import CreateView

from .models import Video
from .utils import VideoTranscriber


class SendVideoRequestHandler(CreateView):
    model = Video
    template_name = "home.html"
    success_url = "/home"
    fields = ["title", "video_file"]

    def form_valid(self, form):
        video = form.save()
        path_video = video.video_file.path
        transcript = VideoTranscriber(path_video)
        transcript.extract_audio_from_video()
        video.transcript = transcript.generate_transcript()
        video.resume = transcript.generate_summary(video.transcript)

        return super().form_valid(form)
