from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artist-list'),
    path('create/', views.ArtistCreateView.as_view(), name='artist-create'),
]