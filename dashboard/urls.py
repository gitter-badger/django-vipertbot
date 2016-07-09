from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^logout/$', views.logout, name='logout'),
]
