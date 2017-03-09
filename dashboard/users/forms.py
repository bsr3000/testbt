import django.forms as forms

from core.models import User, Group, Position


class UsersForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)
    position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label=None)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "group", "position", "photo")
        read_only_fields = ("date_joined",)