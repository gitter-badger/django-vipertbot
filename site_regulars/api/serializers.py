from rest_framework.serializers import ModelSerializer

from site_regulars.models import Regular

class RegularListSerializer(ModelSerializer):
    class Meta:
        model = Regular
        fields = [
            'id',
            'user',
            'name',
            'created_at'
        ]

class RegularDetailSerializer(ModelSerializer):
    class Meta:
        model = Regular
        fields = [
            'id',
            'name'
        ]

class RegularCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Regular
        fields = [
            'name'
        ]