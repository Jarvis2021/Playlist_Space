from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('genreresult', views.genre_result),
    path('genremoods', views.genremoods),
    path('newrelease', views.newreleases),
    path('chart', views.charts),
    path('concert', views.concerts),
]
