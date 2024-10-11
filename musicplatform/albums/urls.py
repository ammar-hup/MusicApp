from django.urls import path
from .views import *

urlpatterns = [
   # API routes
    path('manual-filter/', ManualFilterAlbumView.as_view(), name='manual-filter-album'),  # New endpoint
    path('', ListCreateAlbumView.as_view(), name='album-list-create'),
    path('<int:pk>/', RetrieveUpdateDestroyAlbumView.as_view(), name='album-detail'),
    path('songs/', ListCreateSongView.as_view(), name='song-list'),
    path('songs/<int:pk>/', RetrieveUpdateDestroySongView.as_view(), name='song-detail'),
    # Web routes
    path('create/', CreateAlbumView.as_view(), name='album-web-view'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-web-view'),
    ]
