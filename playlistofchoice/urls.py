from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('genremoods', views.genre_mood),
    path('newrelease', views.newreleases),
    path('chart', views.charts),
    path('concert', views.concerts),
]
