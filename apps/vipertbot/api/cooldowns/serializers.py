from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)

from apps.vipertbot.models import Cooldown

class CooldownListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='cooldowns-detail',
        lookup_field='id'
    )

    class Meta:
        model = Cooldown
        fields = [
            'id',
            'url',
            'name',
            'start_time'
        ]

class CooldownDetailSerializer(ModelSerializer):
    class Meta:
        model = Cooldown
        fields = [
            'id',
            'name',
            'start_time'
        ]

class CooldownCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Cooldown
        fields = [
            'id',
            'name',
            'start_time'
        ]
        read_only_fields = ('id', )