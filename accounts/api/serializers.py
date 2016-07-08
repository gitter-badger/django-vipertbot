from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField
)

from django.contrib.auth import get_user_model
User = get_user_model()

class UserListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='users-detail',
        lookup_field='id'
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'url'
        ]

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        ]

class UserCreateSerializer(ModelSerializer):
    # todo: serialize validated_data for password ...
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class UserUpdateSerializer(ModelSerializer):
    # todo: add staff/admin fields, serialize validated_data for password ...
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }