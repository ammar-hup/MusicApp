from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumList.as_view(), name='view_albums'),
    path('create/', views.CreateAlbumView.as_view(), name='create_album'),
]
