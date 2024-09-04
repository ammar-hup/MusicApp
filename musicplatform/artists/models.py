from django.db.models import Count, Q
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from users.models import User

class ArtistManager(models.Manager):
    def approved_albums(self):
        return self.annotate(approved_albums=Count('album',filter=Q(album__is_approved=True))).order_by('-approved_albums')
    # Artist.objects.filter(albums__is_approved = True).alias(approved_albums = Count('albums')).order_by('approved_albums')

class Artist(models.Model):
    artist_name = models.CharField(unique = True,max_length=255,default='Unknown')
    social_link = models.URLField(default="https://www.instagram.com/")
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'artist',null=True)
    objects = ArtistManager()

    def __str__(self):
        return self.artist_name    

    class Meta :
        ordering = ['id']
        verbose_name = "Artist"

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def UserToken(sender, created, instance, **kwargs):
    if created:
        Token.objects.create(user = instance)