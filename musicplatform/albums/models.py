from django.db import models
from artists.models import Artist
from django_extensions.db.models import TimeStampedModel
from django.db.models import Count, Q

# Create your models here.
class AlbumManager(models.Manager):
    def __str__(self):
        return self.album_name
    class Meta :
        ordering = ['album_name']
        verbose_name = "Album"
    
class Album(models.Model):
    album_name = models.CharField(default='New Album',max_length=200,unique = True)
    creation_datetime = models.DateTimeField(auto_now_add=True,blank=False)
    release_datetime = models.DateTimeField(blank=True, null=True , auto_now_add=True)
    cost = models.FloatField(blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False,help_text='Approve the album if its name is not explicit')
    objects = AlbumManager()

      
    


