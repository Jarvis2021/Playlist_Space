from django.shortcuts import render, redirect
import spotipy

# Create your views here.


def home(request):

    print(" Home Page is Invoked Successfully ")

    return render(request,'home.html')
