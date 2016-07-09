from django.http import JsonResponse, HttpResponse
from .follows import (
    Followers,
    Following,
    Follow,
    UnFollow
)

# Create your views here.
def followers(request):
    data = Followers(request.user.username)
    return JsonResponse(data)

def following(request, target):
    data = Following(request.user.username, target)
    return JsonResponse(data)

def follow(request, target):
    social = request.user.social_auth.get(provider='twitch')
    token = social.extra_data['access_token']

    data = Follow(request.user.username, target, token)
    return HttpResponse(data, content_type='application/json')

def unfollow(request, target):
    social = request.user.social_auth.get(provider='twitch')
    token = social.extra_data['access_token']

    data = UnFollow(request.user.username, target, token)

    return HttpResponse(data, content_type='application/json')
