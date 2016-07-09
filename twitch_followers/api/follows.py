import requests, json
from twitch.api.v3 import follows

base_url = 'https://api.twitch.tv/kraken/users/'

# Create your views here.
def Followers(username):
    data = follows.by_channel(username)
    return data

def Following(username, target):
    data = follows.status(username, target)
    return data

def Follow(username, target, token):
    url = base_url + username + '/follows/channels/' + target

    headers = {'Authorization': 'OAuth '+token}
    r = requests.put(url, headers=headers)

    return r.json

def UnFollow(username, target, token):
    url = base_url + username + '/follows/channels/' + target

    headers = {'Authorization': 'OAuth '+token}
    r = requests.delete(url, headers=headers)

    return r.json

def Streams():
    raise NotImplementedError
