from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
from django.views.generic import ListView,CreateView

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
    success_url = '/albums/create/'

    def form_valid(self, form):
        album_name = form.cleaned_data['album_name']
        cost = form.cleaned_data['cost']
        artist = form.cleaned_data['artist']
        is_approved = form.cleaned_data['is_approved']
        # create an Album instance with the retrieved data
        new_album = Album.objects.create(
            album_name=album_name,
            cost=cost,
            artist=artist,
            is_approved=is_approved,
        )
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response({'form': form})