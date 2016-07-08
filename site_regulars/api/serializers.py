from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)

from site_regulars.models import Regular

from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException

class RegularListSerializer(ModelSerializer):
    user = SerializerMethodField()

    url = HyperlinkedIdentityField(
        view_name='regulars-detail',
        lookup_field='id'
    )

    class Meta:
        model = Regular
        fields = [
            'id',
            'user',
            'name',
            'url'
        ]

    def get_user(self, obj):
        return obj.user.username

class RegularDetailSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Regular
        fields = [
            'id',
            'user',
            'name'
        ]

    def get_user(self, obj):
        return obj.user.username

class RegularCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Regular
        fields = [
            'name'
        ]

    def validate_name(self, value):
        try:
            data = twitch.users.by_name(value)
        except ResourceUnavailableException:
            raise ValidationError("Not a valid Twitch User or not confirmed.")

        return value