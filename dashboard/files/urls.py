from django.conf.urls import url

from dashboard.files.views import user_files, user_upload

urlpatterns = [
    url(r'^my-files/$', user_files, name="list"),
    url(r'^upload-file/$', user_upload, name="create"),
]