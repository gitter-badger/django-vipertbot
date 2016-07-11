from django.conf.urls import url, include

from .views import (
    CommandDetailApiView,
    CommandListApiView,
    CommandCreateApiView,
    CommandUpdateApiView,
    CommandDeleteApiView
)

urlpatterns = [
    url(r'^$', CommandListApiView.as_view(), name='commands-list'),
    url(r'^create/$', CommandCreateApiView.as_view(), name='commands-create'),
    url(r'^(?P<id>\d+)/$', CommandDetailApiView.as_view(), name='commands-detail'),
    url(r'^(?P<id>\d+)/edit/$', CommandUpdateApiView.as_view(), name='commands-update'),
    url(r'^(?P<id>\d+)/delete/$', CommandDeleteApiView.as_view(), name='commands-delete'),
]
