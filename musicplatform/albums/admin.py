from django.contrib import admin

# Register your models here.
from .models import Album
class AlbumAdmin(admin.ModelAdmin):
    model = Album
    list_display = ["id", "name", "creation_datetime" , "release_datetime", "cost", "artist", "is_approved"]
    readonly_fields = ["creation_datetime"]

admin.site.register(Album,AlbumAdmin)