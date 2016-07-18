from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    CurrentUserDefault,
    HiddenField
)
from project.apps.vipertbot.api.users.serializers import UserDetailSerializer
from project.apps.vipertbot.models import Regular
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException


class RegularListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    url = HyperlinkedIdentityField(
        view_name='regulars-detail',
        lookup_field='id'
    )

    class Meta:
        model = Regular
        fields = [
            'id',
            'url',
            'name',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username


class RegularDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Regular
        fields = [
            'id',
            'name',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username


class RegularCreateUpdateSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    url = HyperlinkedIdentityField(
        view_name='regulars-detail',
        lookup_field='id'
    )

    class Meta:
        model = Regular
        fields = [
            'id',
            'url',
            'name',
            'user'
        ]

        read_only_fields = ('id', 'url')

    def validate_name(self, value):
        request = self.context['request']

        if request.user.username.lower() == value.lower():
            raise ValidationError('You can not add yourself!')

        if Regular.objects.filter(name__iexact=value).exists():
            raise ValidationError('Regular already exists.')

        try:
            data = twitch.users.by_name(value)
        except ResourceUnavailableException:
            raise ValidationError("Not a valid Twitch User.")

        return value
