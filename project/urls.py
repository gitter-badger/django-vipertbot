from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # vipertbot.api
    url(r'^api/users/', include('project.apps.vipertbot.api.users.urls'), name='users-api'),
    url(r'^api/followers/', include('project.apps.vipertbot.api.followers.urls'), name='followers-api'),
    url(r'^api/commands/', include('project.apps.vipertbot.api.commands.urls'), name='commands-api'),
    url(r'^api/cooldowns/', include('project.apps.vipertbot.api.cooldowns.urls'), name='cooldowns-api'),
    url(r'^api/jobs/', include('project.apps.vipertbot.api.jobs.urls'), name='jobs-api'),
    url(r'^api/regulars/', include('project.apps.vipertbot.api.regulars.urls'), name='regulars-api'),
    url(r'^api/roles/', include('project.apps.vipertbot.api.roles.urls'), name='roles-api'),

    # vipertbot
    url(r'', include('project.apps.vipertbot.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
