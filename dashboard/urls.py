from django.conf.urls import url, include

from dashboard.views import index
from files.urls import urlpatterns as files_urls
from group.urls import urlpatterns as group_urls
from users.urls import urlpatterns as users_urls

urlpatterns = [
    url('^files/', include(files_urls, namespace="files")),
    url('^users/', include(users_urls, namespace="users")),
    url('^groups/', include(group_urls, namespace="groups")),
    url('^$', index, name="index"),
]