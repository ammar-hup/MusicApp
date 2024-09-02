from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album,Song
from django.views.generic import CreateView,DetailView
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

# Create your views here.
class ListCreateAlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class RetrieveUpdateDestroyAlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ListCreateSongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class RetrieveUpdateDestroySongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class CreateAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/create_album.html'
    success_url = '/albums/'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Ensure at least one song is associated with the album
        if not self.object.songs.exists():
            form.add_error(None, "An album must have at least one song.")
            return self.form_invalid(form)
        return response

class SongDetailView(DetailView):
    model = Song
    template_name = 'albums/song_detail.html'
    context_object_name = 'song'
    
class ListAlbum(APIView):
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(data = serializer.data , status=status.HTTP_200_OK)

    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)