from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url('', include('welcome.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include(router.urls)),
    url(r'^api/users/', include('accounts.api.urls'), name='users-api'),
    url(r'^api/followers/', include('twitch_followers.api.urls'), name='followers-api'),
    url(r'^api/commands/', include('site_commands.api.urls'), name='commands-api'),
    url(r'^api/jobs/', include('site_jobs.api.urls'), name='jobs-api'),
    url(r'^api/regulars/', include('site_regulars.api.urls'), name='regulars-api'),
    url(r'^api/roles/', include('twitch_roles.api.urls'), name='roles-api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
