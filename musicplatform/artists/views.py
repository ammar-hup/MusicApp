from typing import Any
from django.shortcuts import redirect, render
from .models import *
from .forms import ArtistForm
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArtistSerializer
from rest_framework import status, filters
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAuthorOrReadOnly

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

# CBV for Artist API
class ArtistList(APIView):
    # authentication method
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # GET method
    def get(self,requst):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many = True)
        return Response(serializer.data)
    
    # Post method
    def post(self,requst):
        serializer = ArtistSerializer(data = requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
