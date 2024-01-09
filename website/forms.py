from django import forms
import magic

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["video_file"]
        widgets = {"video_file": forms.FileInput(attrs={"accept": "video/*"})}

    def clean(self):
        video_file = self.cleaned_data["video_file"]

        if video_file:
            file_type = magic.from_buffer(video_file.read(), mime=True)

            if file_type != "video/*":
                raise forms.ValidationError(
                    "Unsupported file type. Only mp4 videos are allowed."
                )

            video_file.seek(0)

        return video_file
