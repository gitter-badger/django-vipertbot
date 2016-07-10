from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from site_jobs.models import Job

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
    JobCreateUpdateSerializer,
    JobDetailSerializer,
    JobListSerializer,
)

class JobListApiView(ListAPIView):
    serializer_class = JobListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'name',
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email'
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Job.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)|
                Q(user__username=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list

class JobDetailApiView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    lookup_field = 'id'

class JobCreateApiView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobUpdateApiView(RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class JobDeleteApiView(DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'