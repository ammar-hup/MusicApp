from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(blank=False, unique=True, max_length=255, default='Unknown')
    social_link = models.URLField(max_length=200, blank=True, null=True)  # Updated field name

    def __str__(self):
        return self.artist_name    

    class Meta:
        ordering = ['artist_name']
        verbose_name = "Artist"
