from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(blank = False, unique = True, default='Unknown')
    socialLink = models.URLField(default="https://www.instagram.com")

    def __str__(self):
        return self.artist_name    

    class Meta:
        ordering = ['artist_name']
        verbose_name = "Artist"

