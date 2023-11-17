from django.contrib import admin

# Register your models here.
from .models import Album
class AlbumAdmin(admin.ModelAdmin):
    model = Album

admin.site.register(Album,AlbumAdmin)