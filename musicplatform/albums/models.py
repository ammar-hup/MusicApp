from django.db import models
from django.core.exceptions import ValidationError
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.files.storage import FileSystemStorage

# File storage for media files
media_storage = FileSystemStorage(location='media')

class AlbumManager(models.Manager):
    def approved(self):
        return self.filter(is_approved=True)

class Album(models.Model):
    album_name = models.CharField(default='New Album', max_length=200, unique=True)
    creation_datetime = models.DateTimeField(auto_now_add=True, blank=False)
    release_datetime = models.DateTimeField(blank=True, null=True)
    cost = models.FloatField(blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    is_approved = models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')

    objects = AlbumManager()  # Use the custom manager

    def __str__(self):
        return self.album_name

    class Meta:
        ordering = ['album_name']
        verbose_name = "Album"

class SongManager(models.Manager):
    def approved(self):
        return self.filter(album__is_approved=True)

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    image = models.ImageField(upload_to='songs/', storage=media_storage, null=True, blank=True)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    audio_file = models.FileField(upload_to='songs/audio/', storage=media_storage, null=True, blank=True)

    objects = SongManager()  # Use the custom manager

    def __str__(self):
        return self.name