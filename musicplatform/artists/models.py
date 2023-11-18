from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(unique = True,max_length=20,default='Unknown',blank=False)
    socialLink = models.URLField(default="https://www.instagram.com")

    def __str__(self):
        return self.name    

    class Meta:
        ordering = ['artist_name']
        verbose_name = "Artist"

