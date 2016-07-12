from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.index, name='welcome'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^bot/', include('project.apps.vipertbot.twitch_bot.urls'), name='bot'),
    url(r'^logout/$', views.logout, name='logout')
]
