
from django.contrib import admin
from .models import Album, Song
from .forms import *

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    list_display = ['id', 'album_name', 'creation_datetime' , 'release_datetime', 'cost', 'artist', 'is_approved']
    readonly_fields = ['creation_datetime']
            
class SongAdmin(admin.ModelAdmin):
    model = Song
    form = forms.ModelForm
    list_display = ('id', 'name', 'album')
    fields = ['name', "album"]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
