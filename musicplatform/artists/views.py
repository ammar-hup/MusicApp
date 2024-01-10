from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect ,HttpResponse
from .models import Artist,ArtistManager
from .forms import ArtistForm
from django.views.generic import ListView,CreateView
# Create your class based views here.

class ArtistList(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'artist_list.html'

    def get_queryset(self) -> QuerySet[Any]:
#       Fetch artists and their related albums in one query
        return Artist.objects.prefetch_related('album_set').all()

class CreateArtistView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/create_artist.html'
    success_url = '/artists/create/'

    def form_valid(self, form):
        name = form.cleaned_data['artist_name']
        social_link = form.cleaned_data['social_link']
        Artist.objects.create(artist_name=name, social_link=social_link)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response({'form': form})