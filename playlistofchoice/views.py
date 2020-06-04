from django.shortcuts import render, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys



def index(request):

    return render(request,'home.html')

def genre_result(request):

    cid = '507b63501e804f87bd8538c0c6f395ed'
    secret = 'b14546bedc8844c8be95486386500f50'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,requests_timeout=100)

    results = sp.categories(country='US', limit=50, offset=0)
    genre_mood_list=[]

    for i in results['categories']['items']:
        genre_mood_list.append(
            {
                "category_link" : i['href'],
                "category_name" : i['name'],
                "category_image" : i['icons'][0]['url']
            }
        )
    request.session['category_list'] = genre_mood_list

    return redirect('/genremoods')

def genremoods(request):

    genre_list = request.session['category_list']

    context = {
        "genre_list" : genre_list
    }
    return render(request, 'genreandmood.html',context)


def newreleases (request):
    return render(request,'newreleases.html')

def charts(request):

    return render(request,'charts.html')

def concerts(request):

    return render(request,'concerts.html')
