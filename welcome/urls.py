from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.index, name='welcome'),
]
