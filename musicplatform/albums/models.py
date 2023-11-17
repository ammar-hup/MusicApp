from django.db import models
from artists.models import Artist
# Create your models here.

class Album(models.Model):
<<<<<< task1
    album_name = models.CharField(default='New Album',max_length=20)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField()
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL)
>>>>>> main
    def __str__(self):
        return self.name    
    class Meta :
        ordering = ['name']
        verbose_name = "Album"
