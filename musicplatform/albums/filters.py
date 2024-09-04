import django_filters
from .models import *

class AlbumFilter(django_filters.FilterSet):
    album_name = django_filters.CharFilter(field_name='album_name', lookup_expr='icontains')
    cost = django_filters.RangeFilter()
    class Meta:
        model = Album
        fields = {
            'album_name': ['icontains'],  # Case-insensitive search
            'cost': ['gte', 'lte'],     
            'is_approved': ['exact'],
        }
