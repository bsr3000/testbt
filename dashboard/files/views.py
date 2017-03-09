from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import UserDocs
from dashboard.files.forms import FileForm


@login_required()
def user_files(request):
    files = UserDocs.objects.filter(user=request.user)
    return render(request, "dashboard/files/list.html", context={"files": files})


def user_upload(request):
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard:files:list")
    return render(request, "dashboard/files/create.html", context={"form": form})