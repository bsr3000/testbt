from django.conf.urls import url

from dashboard.users.views import user_list, user_details, user_delete_modal, user_create, user_delete

urlpatterns = [
    url(r'^list/$', user_list, name='list'),
    url(r'^create/$', user_create, name='create'),
    url(r'^details/(?P<pk>\d+)/$', user_details, name='details'),
    url(r'^delete/(?P<pk>\d+)/$', user_delete_modal, name='delete-modal'),
    url(r'^delete/(?P<pk>\d+)/confirm/$', user_delete, name='delete'),
]