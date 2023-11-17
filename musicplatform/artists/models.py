from django.db.models import Count, Q
from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(unique = True,max_length=20)
    socialLink = models.URLField(default="https://www.instagram.com")

    def __str__(self):
        return self.name    

    class Meta :
        ordering = ['name']
        verbose_name = "Artist"

