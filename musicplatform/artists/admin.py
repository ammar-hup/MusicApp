from django.contrib import admin

# Register your models here.

from .models import Artist
class ArtistAdmin(admin.ModelAdmin):
    model = Artist

admin.site.register(Artist,ArtistAdmin)