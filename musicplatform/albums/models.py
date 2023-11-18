from django.db import models
from artists.models import Artist

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(default='New Album',max_length=20)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(null=True,blank=True)
    cost = models.FloatField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.album_name    
    class Meta :
        ordering = ['album_name']
        verbose_name = "Album"
