from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.followers, name='followers'),
    url(r'^following/(?P<target>[\w-]+)/$', views.following, name='following'),
    url(r'^follow/(?P<target>[\w-]+)/$', views.follow, name='follow'),
    url(r'^unfollow/(?P<target>[\w-]+)/$', views.unfollow, name='unfollow'),
]
