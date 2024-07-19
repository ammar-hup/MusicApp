from django.contrib import admin
from .models import Album

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    model = Album

admin.site.register(Album,AlbumAdmin)