from django.forms import ModelForm

from core.models import UserDocs


class FileForm(ModelForm):
    class Meta:
        model = UserDocs
        fields = ("user", "doc",)
