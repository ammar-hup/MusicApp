from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album, Song
from django.views.generic import CreateView, DetailView
from .serializers import AlbumSerializer, SongSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions  # Add this line to import the permissions module
from .filters import AlbumFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

class IsArtist(permissions.BasePermission):
    """
    Custom permission to only allow artists to create albums.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is an artist
        return hasattr(request.user, 'artist')  # Assuming you have a related name 'artist' in your User model
# API Views
class ListCreateAlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.approved()  # Use the custom manager for approved albums
    serializer_class = AlbumSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AlbumFilter
    context_object_name = 'albums'
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            # Allow only authenticated users to create an album
            return [IsArtist()]
        # Allow any user to view the albums
        return [AllowAny()]

class ManualFilterAlbumView(APIView):
    def get(self, request):
        # Get query parameters
        cost_gte = request.query_params.get('cost__gte')
        cost_lte = request.query_params.get('cost__lte')
        album_name = request.query_params.get('album_name')

        # Validate cost filters
        if cost_gte is not None:
            try:
                cost_gte = float(cost_gte)  # Convert to float
            except ValueError:
                return Response({"error": "Invalid value for cost__gte. Must be a number."}, status=status.HTTP_400_BAD_REQUEST)

        if cost_lte is not None:
            try:
                cost_lte = float(cost_lte)  # Convert to float
            except ValueError:
                return Response({"error": "Invalid value for cost__lte. Must be a number."}, status=status.HTTP_400_BAD_REQUEST)

        # Start with all albums
        albums = Album.objects.all()

        # Apply cost filters if provided
        if cost_gte is not None:
            albums = albums.filter(cost__gte=cost_gte)
        if cost_lte is not None:
            albums = albums.filter(cost__lte=cost_lte)

        # Apply album name filter if provided
        if album_name is not None:
            albums = albums.filter(album_name__icontains=album_name)

        # Serialize the filtered albums
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class RetrieveUpdateDestroyAlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.approved()  # Ensure only approved albums can be retrieved/updated/destroyed
    permission_classes = [AllowAny]
    serializer_class = AlbumSerializer

class ListCreateSongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()  # You may want to filter this based on approved albums
    serializer_class = SongSerializer

class RetrieveUpdateDestroySongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# Django Views

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

