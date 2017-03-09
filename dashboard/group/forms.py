from django.forms import ModelForm

from core.models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"