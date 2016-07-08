from django.conf.urls import url, include

from .views import (
    RegularDetailApiView,
    RegularListApiView,
    RegularCreateApiView,
    RegularUpdateApiView,
    RegularDeleteApiView
)

urlpatterns = [
    url(r'^$', RegularListApiView.as_view(), name='regulars-list'),
    url(r'^create/$', RegularCreateApiView.as_view(), name='regulars-create'),
    url(r'^(?P<id>\d+)/$', RegularDetailApiView.as_view(), name='regulars-detail'),
    url(r'^(?P<id>\d+)/edit/$', RegularUpdateApiView.as_view(), name='regulars-update'),
    url(r'^(?P<id>\d+)/delete/$', RegularDeleteApiView.as_view(), name='regulars-delete'),
]
