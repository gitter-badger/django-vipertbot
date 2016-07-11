from django.conf.urls import url, include

from .views import (
    CooldownDetailApiView,
    CooldownListApiView,
    CooldownCreateApiView,
    CooldownUpdateApiView,
    CooldownDeleteApiView
)

urlpatterns = [
    url(r'^$', CooldownListApiView.as_view(), name='cooldowns-list'),
    url(r'^create/$', CooldownCreateApiView.as_view(), name='cooldowns-create'),
    url(r'^(?P<id>\d+)/$', CooldownDetailApiView.as_view(), name='cooldowns-detail'),
    url(r'^(?P<id>\d+)/edit/$', CooldownUpdateApiView.as_view(), name='cooldowns-update'),
    url(r'^(?P<id>\d+)/delete/$', CooldownDeleteApiView.as_view(), name='cooldowns-delete'),
]
