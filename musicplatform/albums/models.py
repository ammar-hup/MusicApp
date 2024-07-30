from django.db import models
from artists.models import Artist
from datetime import datetime
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(default='New Album',max_length=200,unique = True)
    creation_datetime = models.DateTimeField(auto_now_add=True,blank=False)
    release_datetime = models.DateTimeField(blank=True, null=True , auto_now_add=True)
    cost = models.FloatField(blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False,help_text='Approve the album if its name is not explicit')
    
    def __str__(self):
        return self.album_name    
    class Meta :
        ordering = ['album_name']
        verbose_name = "Album"

class song(models.Model):
    name = models.CharField(max_length=150,default='New Song')
    image = models.ImageField(upload_to='songs/%y/%m/%d' , blank=False)
    image_thumbnail = ImageSpecField(
        source='image',
        processors = [ResizeToFill(100, 50)],
        format = 'JPEG',
        options = {'quality': 60}
        )
    album = models.ForeignKey(Album,on_delete=models.PROTECT,related_name='songs')
    audio_file = models.FileField(upload_to= 'audio/%y/%m/%d',blank=False)

    def __str__(self):
        return self.song_name
    