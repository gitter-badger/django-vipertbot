from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)
from accounts.api.serializers import UserDetailSerializer

from site_regulars.models import Regular

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

    class Meta:
        model = Regular
        fields = [
            'name',
            'user'
        ]

    def validate_name(self, value):
        try:
            data = twitch.users.by_name(value)
        except ResourceUnavailableException:
            raise ValidationError("Not a valid Twitch User or not confirmed.")

        return value