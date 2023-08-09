from django.db import models
from artists.models import Artist
# Create your models here.
class Album(models.Model):
    name = models.CharField(default='New Album',max_length=200)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(blank=True, null=True)
    cost = models.FloatField(blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name    
    class Meta :
        ordering = ['name']
        verbose_name = "Album"