from django.db import models
# from albums.models import Album

# Create your models here.
class Artist(models.Model):
    name = models.CharField(blank = False,unique = True,max_length=200)
    socialLink = models.URLField(null=False,default="https://www.instagram.com")
    # approved_albums = models.ForeignKey(Album,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name    

    class Meta :
        ordering = ['name']
        verbose_name = "Artist"

