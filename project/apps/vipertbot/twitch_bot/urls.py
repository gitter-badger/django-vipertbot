from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start/$', views.start, name='start'),
    url(r'^stop/$', views.stop, name='stop')
]