import json

import django_filters
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from core.models import User, Group, UserDocs
from core.serializers import UserSerializer, GroupListSerializer, GroupDetailsSerializer, \
    UserDocsSerializer


"""Creating custom permission, so only staff user can use some views"""
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


"""Filter of data for users list"""
class UserFilter(django_filters.rest_framework.FilterSet):
    minsalary = django_filters.NumberFilter(name="salary", lookup_expr='gte')
    maxsalary = django_filters.NumberFilter(name="salary", lookup_expr='lte')
    group = django_filters.ModelChoiceFilter(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['group', 'minsalary', 'maxsalary']


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    search_fields = ('email', 'position__pos_name')
    filter_class = UserFilter
    ordering_fields = ('id', 'email', 'salary')
    permission_classes = [IsAuthenticated, ]
    #authentication_classes = [TokenAuthentication, BaseAuthentication]

    @detail_route(methods=['get'], permission_classes=[IsAuthenticated, IsStaff])
    def retrieve_docs(self, request, pk=None, **kwargs):
        docs = UserDocs.objects.filter(user=request.user)
        serializer = UserDocsSerializer(docs, many=True)
        return Response(data=serializer.data)

    @detail_route(methods=['post'], permission_classes=[IsAuthenticated, IsStaff])
    def create_docs(self, request, *args, **kwargs):
        serializer = UserDocsSerializer(request.data)
        serializer.validated_data['user'] = request.user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(status=400)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().prefetch_related('user_set')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('gr_name',)
    ordering_fields = ('id', 'gr_name')
    permission_classes = [IsAuthenticated, ]
    #authentication_classes = [TokenAuthentication, BaseAuthentication]

    @detail_route(methods=['post'], permission_classes=[IsAuthenticated, IsStaff])
    def delete_user(self, request, pk, **kwargs):
        group = get_object_or_404(self.queryset.all(), pk=pk)
        user = get_object_or_404(User.objects.all(), pk=request.data.get('user_id', None))
        try:
            group.user_set.remove(user)
            serializer = GroupDetailsSerializer(instance=group)
            return Response(data=serializer.data, status=200)
        except Exception:
            return Response(data=json.dumps(Exception.message), status=500)

    @detail_route(methods=['post'], permission_classes=[IsAuthenticated, IsStaff])
    def add_user(self, request, pk, **kwargs):
        group = get_object_or_404(self.queryset.all(), pk=pk)
        user = get_object_or_404(User.objects.all(), pk=request.data.get('user_id', None))
        try:
            group.user_set.add(user)
            serializer = GroupDetailsSerializer(instance=group)
            return Response(data=serializer.data)
        except Exception:
            return Response(data=json.dumps(Exception.message), status=500)