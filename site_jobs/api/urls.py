from django.conf.urls import url, include

from .views import (
    JobDetailApiView,
    JobListApiView,
    JobCreateApiView,
    JobUpdateApiView,
    JobDeleteApiView
)

urlpatterns = [
    url(r'^$', JobListApiView.as_view(), name='jobs-list'),
    url(r'^create/$', JobCreateApiView.as_view(), name='jobs-create'),
    url(r'^(?P<id>\d+)/$', JobDetailApiView.as_view(), name='jobs-detail'),
    url(r'^(?P<id>\d+)/edit/$', JobUpdateApiView.as_view(), name='jobs-update'),
    url(r'^(?P<id>\d+)/delete/$', JobDeleteApiView.as_view(), name='jobs-delete'),
]
