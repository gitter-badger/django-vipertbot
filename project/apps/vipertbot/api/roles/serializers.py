from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)

from apps.vipertbot.models import Role

class RoleListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='roles-detail',
        lookup_field='id'
    )

    class Meta:
        model = Role
        fields = [
            'id',
            'url',
            'name',
        ]

class RoleDetailSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name'
        ]

class RoleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name'
        ]
        read_only_fields = ('id', )