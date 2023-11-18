from django.db import models
from artists.models import Artist
from django.utils import timezone

# Create your models here.

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=255, default='New Album')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(default='2000-12-12')
    cost = models.FloatField()
    is_approved = models.BooleanField(default=False,help_text='Approve the album if its name is not explicit')
    def __str__(self):
        return self.album_name    
    class Meta :
        ordering = ['album_name']
        verbose_name = "Album"
