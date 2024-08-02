
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album,Song
from django.views.generic import ListView,CreateView,DetailView

# Create your views here.
class AlbumList(ListView):
    model = Album
    context_object_name  = 'albums'
    template_name = 'albums/view_albums.html'

    def get_queryset(self):
        return Album.objects.all()
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
    
