from django.db.models import Count, Q
from django.db import models


class ArtistManager(models.Manager):
    def with_approved_albums_count(self):
        return self.annotate(
            approved_albums_count=Count('album', filter=Q(album__is_approved=True))
        ).order_by('approved_albums_count')

class Artist(models.Model):
    artist_name = models.CharField(unique = True,max_length=255,default='Unknown')
    social_link = models.URLField(default="https://www.instagram.com")
    objects = ArtistManager()

    def __str__(self):
        return self.name    

    class Meta :
        ordering = ['artist_name']
        verbose_name = "Artist"

