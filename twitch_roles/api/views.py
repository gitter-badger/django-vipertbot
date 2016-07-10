from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from twitch_roles.models import Role

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .serializers import (
    RoleCreateUpdateSerializer,
    RoleDetailSerializer,
    RoleListSerializer,
)

class RoleListApiView(ListAPIView):
    serializer_class = RoleListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'name'
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Role.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            ).distinct()

        return queryset_list

class RoleDetailApiView(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleDetailSerializer
    lookup_field = 'id'

class RoleCreateApiView(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleCreateUpdateSerializer

class RoleUpdateApiView(RetrieveUpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleCreateUpdateSerializer
    lookup_field = 'id'

class RoleDeleteApiView(DestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleDetailSerializer
    lookup_field = 'id'