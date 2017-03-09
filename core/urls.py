from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views

from core.views import get_position_list, get_non_group_members, get_user_by_token
from core.viewsets import UserViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/', include(router.urls, namespace="api-core")),
    url(r'^api/positions/$', get_position_list, name="get_position_list"),
    url(r'^api/groups/$', get_non_group_members, name="get_non_group_members"),
    url(r'^api/users/token/(?P<token>[-\w]+)/$', get_user_by_token, name="get_user_by_token"),
]
