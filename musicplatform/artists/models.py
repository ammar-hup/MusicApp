from django.db.models import Count, Q
from django.db import models


class ArtistManager(models.Manager):
    def with_approved_albums_count(self):
        return self.annotate(
            approved_albums_count=Count('album', filter=Q(album__is_approved=True))
        ).order_by('approved_albums_count')

class Artist(models.Model):
    artist_name = models.CharField(blank = False,unique = True,max_length=200 , verbose_name='Artist Name')
    socialLink = models.URLField(null=False,default="https://www.instagram.com" , verbose_name='Social Media')

    def __str__(self):
        return self.name    

    class Meta :
        ordering = ['name']
        verbose_name = "Artist"

