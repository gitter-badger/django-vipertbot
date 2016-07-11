from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)
from project.apps.vipertbot.api.users.serializers import UserDetailSerializer

from project.apps.vipertbot.models import Job

class JobListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    url = HyperlinkedIdentityField(
        view_name='jobs-detail',
        lookup_field='id'
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'url',
            'name',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username

class JobDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id',
            'name',
            'user'
        ]

    def get_user(self, obj):
        return obj.user.username

class JobCreateUpdateSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'name',
            'user'
        ]