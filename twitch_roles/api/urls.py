from django.conf.urls import url, include

from .views import (
    RoleDetailApiView,
    RoleListApiView,
    RoleCreateApiView,
    RoleUpdateApiView,
    RoleDeleteApiView
)

urlpatterns = [
    url(r'^$', RoleListApiView.as_view(), name='roles-list'),
    url(r'^create/$', RoleCreateApiView.as_view(), name='roles-create'),
    url(r'^(?P<id>\d+)/$', RoleDetailApiView.as_view(), name='roles-detail'),
    url(r'^(?P<id>\d+)/edit/$', RoleUpdateApiView.as_view(), name='roles-update'),
    url(r'^(?P<id>\d+)/delete/$', RoleDeleteApiView.as_view(), name='roles-delete'),
]
