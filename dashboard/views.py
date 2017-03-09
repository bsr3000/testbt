from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import User, Group, UserDocs


@login_required()
def index(request):
    context = {"users": User.objects.count(), "groups": Group.objects.count(),
               "files": UserDocs.objects.count()}
    return render(request, "dashboard/index.html", context=context)