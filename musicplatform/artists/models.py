from django.db.models import Count, Q
from django.db import models


class ArtistManager(models.Manager):
    def with_approved_albums_count(self):
        return self.annotate(
            approved_albums_count=Count('album', filter=Q(album__is_approved=True))
        ).order_by('approved_albums_count')

class Artist(models.Model):
<<<<<<< HEAD
    artist_name = models.CharField(blank = False,unique = True,max_length=200 , verbose_name='Artist Name')
    socialLink = models.URLField(null=False,default="https://www.instagram.com" , verbose_name='Social Media')
=======
    artist_name = models.CharField(unique = True,max_length=255,default='Unknown')
    social_link = models.URLField(default="https://www.instagram.com")
>>>>>>> task2
    objects = ArtistManager()

    def __str__(self):
        return self.artist_name    

    class Meta :
        ordering = ['artist_name']
        verbose_name = "Artist"

