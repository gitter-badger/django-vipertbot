from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from django.contrib.auth.models import User

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .serializers import (
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDetailSerializer,
    UserListSerializer,
)

class UserListApiView(ListAPIView):
    serializer_class = UserListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated, IsAdminUser]
    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name',
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(username__icontains=query)|
                Q(email__icontains=query)|
                Q(first_name__icontains=query)|
                Q(last_name__icontains=query)
            ).distinct()

        return queryset_list

class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserUpdateApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

class UserDeleteApiView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'