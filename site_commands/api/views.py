from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from site_commands.models import Command

from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import (
    IsAuthenticated,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .serializers import (
    CommandCreateUpdateSerializer,
    CommandDetailSerializer,
    CommandListSerializer,
)

class CommandListApiView(ListAPIView):
    serializer_class = CommandListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'name',
        'text',
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email'
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Command.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)|
                Q(text__icontains=query)|
                Q(user__username=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list

class CommandDetailApiView(RetrieveAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandDetailSerializer
    lookup_field = 'id'

class CommandCreateApiView(CreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommandUpdateApiView(RetrieveUpdateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class CommandDeleteApiView(DestroyAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'