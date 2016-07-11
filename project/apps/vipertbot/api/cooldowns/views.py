from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from project.apps.vipertbot.models import Cooldown

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .serializers import (
    CooldownCreateUpdateSerializer,
    CooldownDetailSerializer,
    CooldownListSerializer,
)

class CooldownListApiView(ListAPIView):
    serializer_class = CooldownListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'name',
        'user__username'
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Cooldown.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)|
                Q(user__username=query)
            ).distinct()

        return queryset_list

class CooldownDetailApiView(RetrieveAPIView):
    queryset = Cooldown.objects.all()
    serializer_class = CooldownDetailSerializer
    lookup_field = 'id'

class CooldownCreateApiView(CreateAPIView):
    queryset = Cooldown.objects.all()
    serializer_class = CooldownCreateUpdateSerializer

class CooldownUpdateApiView(RetrieveUpdateAPIView):
    queryset = Cooldown.objects.all()
    serializer_class = CooldownCreateUpdateSerializer
    lookup_field = 'id'

class CooldownDeleteApiView(DestroyAPIView):
    queryset = Cooldown.objects.all()
    serializer_class = CooldownDetailSerializer
    lookup_field = 'id'