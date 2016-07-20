from project.apps.vipertbot.api.helpers.validation import ApiValidationError

from rest_framework.serializers import (
    ModelSerializer,
)
from project.apps.vipertbot.api.users.serializers import UserDetailSerializer
from project.apps.vipertbot.api.roles.serializers import RoleDetailSerializer
from project.apps.vipertbot.models import Command
from project.apps.vipertbot.models import Role


class CommandListSerializer(ModelSerializer):
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
            'id',
            'name',
            'text',
            'cooldown_min',
            'active',
            'roles',
            'user'
        ]

        read_only_fields = ('id', 'url')

    def validate_name(self, value):
        if ' ' in value:
            raise ApiValidationError('Command can not contain spaces!')

        if not str(value).startswith('!'):
            raise ApiValidationError('Command must start with !')

        return value

    def create(self, validated_data):
        request = self.context['request']
        cmd = Command(
            name=validated_data.get('name'),
            text=validated_data.get('text'),
            cooldown_min=validated_data.get('cooldown_min'),
            active=validated_data.get('active'),
            user_id=request.user.id
        )
        cmd.save()

        try:
            roles = validated_data['roles']
            for item in roles:
                name = item.get('name')
                cmd.roles.add(Role.objects.get(name=name))
        except KeyError:
            pass

        return cmd

    def update(self, instance, validated_data):
        try:
            roles = validated_data['roles']

            instance.roles.clear()
            for item in roles:
                name = item.get('name')
                instance.roles.add(Role.objects.get(name=name))

        except KeyError:
            pass

        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.cooldown_min = validated_data.get('cooldown_min', instance.cooldown_min)
        instance.active = validated_data.get('active', instance.active)
        instance.user = instance.user
        instance.save()
        return instance
