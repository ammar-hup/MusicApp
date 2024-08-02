from django.db.models import Count, Q
from django.db import models


class ArtistManager(models.Manager):
    def approved_albums(self):
        return self.annotate(approved_albums=Count('album',filter=Q(album__is_approved=True))).order_by('-approved_albums')
    # Artist.objects.filter(albums__is_approved = True).alias(approved_albums = Count('albums')).order_by('approved_albums')

class Artist(models.Model):
    artist_name = models.CharField(unique = True,max_length=255,default='Unknown')
    social_link = models.URLField(default="https://www.instagram.com/")
    objects = ArtistManager()

    def __str__(self):
        return self.artist_name    

    class Meta :
        ordering = ['artist_name']
        verbose_name = "Artist"

