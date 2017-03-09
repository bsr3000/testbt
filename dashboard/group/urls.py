from django.conf.urls import url

from dashboard.group.views import group_list, group_delete_modal, group_details, group_delete, group_create

urlpatterns = [
    url(r'list/$', group_list, name="list"),
    url(r'create/$', group_create, name="create"),
    url(r'details/(?P<pk>\d+)/$', group_details, name="details"),
    url(r'delete/(?P<pk>\d+)/$', group_delete_modal, name="delete-modal"),
    url(r'delete/(?P<pk>\d+)/delete/$', group_delete, name="delete"),
]