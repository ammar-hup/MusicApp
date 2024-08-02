# Register your models here.
from django.contrib import admin
from .models import Artist
from albums.models import Album

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id','artist_name', 'social_link', 'approved_albums']

    def approved_albums(self, obj):
        return Album.objects.filter(artist=obj, is_approved=True).count()

admin.site.register(Artist,ArtistAdmin)