from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Position, User
from core.serializers import UserRegisterSerializer, PositionSerializer, UserSerializer


@api_view(http_method_names=['post'])
def register_user(request):
    serializer = UserRegisterSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(status=400)


@api_view(http_method_names=['get'])
def get_position_list(request):
    serializer = PositionSerializer(Position.objects.all(), many=True)
    return Response(serializer.data, status=200)


@api_view(http_method_names=['get'])
def get_non_group_members(request, pk):
    queryset = User.objects.all().exclude(group_id=pk)
    serializer = UserSerializer(queryset)
    return Response(serializer.data, status=200)


@api_view(http_method_names=['get'])
def get_user_by_token(request, token):
    user = get_object_or_404(Token, key=token)
    user = user.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=200)