from django.urls import path
from .views import AlbumList, CreateAlbumView, SongDetailView

urlpatterns = [
    path('', AlbumList.as_view(), name='view_albums'),
    path('create/', CreateAlbumView.as_view(), name='create_album'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
]
