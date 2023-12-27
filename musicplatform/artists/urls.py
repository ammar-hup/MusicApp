from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('create/', views.create_artist, name='create_artist'),
]