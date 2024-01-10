from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artistList'),
    path('create/', views.CreateArtistView.as_view(), name='CreateArtistView'),
]