from django.views.generic.edit import CreateView
from .models import Video


class SendVideoRequestHandler(CreateView):
    model = Video
    template_name = "home.html"
    success_url = "/home"
    fields = ["title", "video_file"]
