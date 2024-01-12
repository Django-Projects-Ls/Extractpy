from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

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


def home_redirect_view(request):
    # Redirect to the upload view
    return redirect(reverse_lazy("upload_video"))
