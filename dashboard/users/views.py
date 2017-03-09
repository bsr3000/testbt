from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, redirect, render

from core.models import User
from dashboard.users.forms import UsersForm


@login_required
def user_list(request):
    queryset = User.objects.all().exclude(id=request.user.id)
    paginator = Paginator(queryset, 9)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, "dashboard/users/list.html", context={"users": users})


@login_required
def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UsersForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
    return render(request, "dashboard/users/details.html", context={"form": form, "instance": user})


@login_required()
def user_delete_modal(request, pk):
    user = get_object_or_404(User, pk=pk)
    docs = user.userdocs_set.all()
    context = {"user": user, "docs": docs}
    return render(request,"dashboard/users/modal_delete.html", context=context)


@login_required()
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, message="Deleted user %s" % user.email)
    return redirect('dashboard:users:list')


@login_required()
def user_create(request):
    form = UsersForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, message="Created user %s" % user.email)
        return redirect('dashboard:users:details', pk=user.pk)
    return render(request, "dashboard/users/details.html", context={"form": form})