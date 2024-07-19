from django.db import models
from artists.models import Artist

# Create your models here.

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(default = 'New Album')
    creation_datetime = models.DateTimeField(auto_now_add = True)
    release_datetime = models.DateTimeField(blank = False)
    cost = models.FloatField(blank = False)
    
    def __str__(self):  
        return self.album_name    
    class Meta :
        ordering = ['album_name']
        verbose_name = "Album"
