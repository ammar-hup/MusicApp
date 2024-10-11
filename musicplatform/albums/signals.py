from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Album
from django.conf import settings

@receiver(post_save, sender=Album)
def send_album_created_notification(sender, instance, created, **kwargs):
    if created:  # Check if the album is newly created
        artist_name = instance.artist.artist_name  # Get the artist's name
        send_mail(
            'Album Created',
            f'A new album "{instance.album_name}" by {artist_name} has been created!',
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],  # This is your email address
            fail_silently=False,
        )
    