from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .filters import *
from rest_framework import status, filters,generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAuthorOrReadOnly

#views for html
class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'artist_list.html'

    def get_queryset(self):
#       Fetch artists and their related albums in one query
        return Artist.objects.prefetch_related('album_set').all()

class ArtistViewList (generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend ,)
    filterset_class = ArtistFilter
class RetrieveUpdateDestroyArtistView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
    
class ArtistViewCreate(APIView):
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)