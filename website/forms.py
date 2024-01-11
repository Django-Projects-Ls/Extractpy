from django import forms
import magic

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["video_file"]
        widgets = {"video_file": forms.FileInput(attrs={"accept": "video/mp4"})}

    def clean(self):
        cleaned_data = super().clean()
        video_file = cleaned_data.get("video_file")

        if video_file:
            file_type = magic.from_buffer(video_file.read(), mime=True)

            if file_type != "video/mp4":
                raise forms.ValidationError(
                    "Unsupported file type. Only mp4 videos are allowed."
                )

            video_file.seek(0)

        return cleaned_data
