import requests
import json
from requests_oauthlib import OAuth1

from django.shortcuts import render, redirect
from django.http import HttpResponse

from allauth.socialaccount.models import SocialToken, SocialApp


def authenticate(user):
    lis = SocialToken.objects.filter(account__user=user, account__provider='twitter')
    socialapp = SocialApp.objects.filter(provider='twitter')
    ACCESS_TOKEN = lis[0].token
    ACCESS_TOKEN_SECRET = lis[0].token_secret
    API_KEY = socialapp[0].client_id
    API_SECRET = socialapp[0].secret
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    requests.get(url, auth=auth)
    return auth


def home(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    return render(request, 'index.html')


def dash(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    return redirect('home')


def dashboard(request):
    if request.user.is_authenticated():
        url = 'https://api.twitter.com/1.1/statuses/home_timeline.json?%s&count=100' % (request.user.username)
        response = requests.get(url, auth=authenticate(request.user))
        return HttpResponse(json.dumps(response.json()))
    return redirect('home')


def tweet(request, tweet_id):
    if request.user.is_authenticated():
        url = 'https://api.twitter.com/1.1/statuses/show.json?id=%s' % (tweet_id)
        response = requests.get(url, auth=authenticate(request.user))
        return render(request, 'tweet.html', {'data': response.json()})
