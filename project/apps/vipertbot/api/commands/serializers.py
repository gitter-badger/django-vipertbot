from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)
from project.apps.vipertbot.api.users.serializers import UserDetailSerializer
from project.apps.vipertbot.api.roles.serializers import RoleDetailSerializer

from project.apps.vipertbot.models import Command
from project.apps.vipertbot.models import Role

class CommandListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    roles = RoleDetailSerializer(read_only=True, many=True)

    url = HyperlinkedIdentityField(
        view_name='commands-detail',
        lookup_field='id'
    )

    class Meta:
        model = Command
        fields = [
            'id',
            'url',
            'name',
            'text',
            'cooldown_min',
            'active',
            'roles',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username

class CommandDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    roles = RoleDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Command
        fields = [
            'id',
            'name',
            'text',
            'cooldown_min',
            'active',
            'roles',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username

class CommandCreateUpdateSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    roles = RoleDetailSerializer(many=True)

    class Meta:
        model = Command
        fields = [
            'name',
            'text',
            'cooldown_min',
            'active',
            'roles',
            'user'
        ]

    def update(self, instance, validated_data):
        instance.roles.clear()

        roles = validated_data['roles']

        for item in roles:
            name = item.get('name')
            instance.roles.add(Role.objects.get(name=name))

        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.cooldown_min = validated_data.get('cooldown_min', instance.cooldown_min)
        instance.active = validated_data.get('active', instance.active)
        instance.user = instance.user
        instance.save()
        return instance