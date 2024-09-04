import django_filters
from .models import *

class ArtistFilter(django_filters.FilterSet):
    artist_name = django_filters.CharFilter(lookup_expr='icontains')
    album_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Artist
        fields = ['artist_name', 'social_link', 'album_name']
