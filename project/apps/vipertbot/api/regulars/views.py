from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from project.apps.vipertbot.models import Regular

from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .serializers import (
    RegularCreateUpdateSerializer,
    RegularDetailSerializer,
    RegularListSerializer,
)

class RegularListApiView(ListAPIView):
    serializer_class = RegularListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'name',
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email'
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Regular.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)|
                Q(user__username=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list

class RegularDetailApiView(RetrieveAPIView):
    queryset = Regular.objects.all()
    serializer_class = RegularDetailSerializer
    lookup_field = 'id'

class RegularCreateApiView(CreateAPIView):
    queryset = Regular.objects.all()
    serializer_class = RegularCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegularUpdateApiView(RetrieveUpdateAPIView):
    queryset = Regular.objects.all()
    serializer_class = RegularCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class RegularDeleteApiView(DestroyAPIView):
    queryset = Regular.objects.all()
    serializer_class = RegularDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'