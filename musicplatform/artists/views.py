from typing import Any
from django.shortcuts import redirect, render
from .models import Artist
from .forms import ArtistForm
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your class based views here.

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'artist_list.html'

    def get_queryset(self):
#       Fetch artists and their related albums in one query
        return Artist.objects.prefetch_related('album_set').all()

class ArtistCreateView(LoginRequiredMixin,CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/create_artist.html'
    # success_url = '/artists/create/'
    success_url = reverse_lazy('artist-list')

    def form_valid(self, form):
        name = form.cleaned_data['artist_name']
        social_link = form.cleaned_data['social_link']
        Artist.objects.create(artist_name=name, social_link=social_link)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response({'form': form})