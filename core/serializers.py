from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from core.models import User, Group, UserDocs, Position
from testproj import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocs
        fields = ('pk', 'doc')


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('pk', 'gr_name')
        depth = 2


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', 'first_name', 'last_name', 'username')


class UserListGroupSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    def get_position(self, obj):
        return u"%s" % obj.position

    def get_full_name(self, obj):
        return u"%s %s" % (obj.first_name, obj.last_name)

    class Meta:
        model = User
        fields = ('pk', 'full_name', 'position')


class GroupDetailsSerializer(serializers.ModelSerializer):
    user_set = UserListGroupSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('pk', 'gr_name', 'user_set')
        depth = 2


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('pk', 'pos_name')


class UserSerializer(serializers.ModelSerializer):
    group = GroupListSerializer()
    position = PositionSerializer()
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return 'media/default.jpg'

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'photo', 'position', 'salary', 'group')

    def create(self, validated_data):
        position = validated_data.pop('position')
        group = validated_data.pop('group')
        user = User.objects.create(group=get_object_or_404(Group, gr_name=group.get('gr_name')) or None,
                                   position=get_object_or_404(Position, pos_name=position.get('pos_name')) or None,
                                   **validated_data)
        return user

    def update(self, instance, validated_data):
        validated_data['position'], crt = Position.objects.get_or_create(**validated_data['position'])
        try:
            validated_data['group'] = Group.objects.get(**validated_data['group'])
        except Group.DoesNotExist:
            validated_data.pop('group')
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user