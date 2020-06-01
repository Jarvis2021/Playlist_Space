from django.shortcuts import render, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys

# Create your views here.
def index(request):

    print(request.POST)

    return render(request,'home.html')

def home_page(request):

    print(request.POST)

    return redirect('/genre_mood')


def genre_mood(request):


    cid = '507b63501e804f87bd8538c0c6f395ed'
    secret = 'b14546bedc8844c8be95486386500f50'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.categories(country='US', limit=50, offset=0)

    # print(results['categories']['items'][0]['href'])
    # print(results['categories']['items'][0]['name'])
    # print(results['categories']['items'][0]['icons'][0]['url'])

    genre_mood_list=[]

    for i in results['categories']['items']:
        genre_mood_list.append(
            {
                "category_link" : i['href'],
                "category_name" : i['name'],
                "category_image" : i['icons'][0]['url']
            }
        )
    print(genre_mood_list)
    context = {'category_list' : genre_mood_list}


    return render(request,'genreandmood.html',context)


def newreleases (request):
    return render(request,'newreleases.html')

def charts(request):

    return render(request,'charts.html')

def concerts(request):

    return render(request,'concerts.html')

def results(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request,'results.html')
