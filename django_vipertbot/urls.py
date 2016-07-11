from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # vipertbot.api
    url(r'^api/users/', include('apps.vipertbot.api.users.urls'), name='users-api'),
    url(r'^api/followers/', include('apps.vipertbot.api.followers.urls'), name='followers-api'),
    url(r'^api/commands/', include('apps.vipertbot.api.commands.urls'), name='commands-api'),
    url(r'^api/cooldowns/', include('apps.vipertbot.api.cooldowns.urls'), name='cooldowns-api'),
    url(r'^api/jobs/', include('apps.vipertbot.api.jobs.urls'), name='jobs-api'),
    url(r'^api/regulars/', include('apps.vipertbot.api.regulars.urls'), name='regulars-api'),
    url(r'^api/roles/', include('apps.vipertbot.api.roles.urls'), name='roles-api'),

    # vipertbot
    url(r'', include('apps.vipertbot.urls')),
]
