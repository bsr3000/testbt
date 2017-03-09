from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Group
from dashboard.group.forms import GroupForm


@login_required
def group_list(request):
    queryset = Group.objects.all()
    paginator = Paginator(queryset, 9)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    return render(request, "dashboard/groups/list.html", context={"groups": groups })


@login_required
def group_details(request, pk):
    gr = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=gr)
    if form.is_valid():
        form.save()
    return render(request, "dashboard/groups/details.html", context={"form": form, "instance": gr, "users_related": gr.user_set.all()})


@login_required()
def group_delete_modal(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request,"dashboard/groups/modal_delete.html", context={"group": group})


@login_required()
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    messages.success(request, message="Deleted group %s" % group.email)
    return redirect('dashboard:groups:list')


@login_required()
def group_create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        group = form.save()
        messages.success(request, message="Created group %s" % group.email)
        return redirect('dashboard:groups:details', pk=group.pk)
    return render(request, "dashboard/groups/details.html", context={"form": form})