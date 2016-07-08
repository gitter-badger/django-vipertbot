from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField
)

from site_regulars.models import Regular

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