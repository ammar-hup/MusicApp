import logging
from celery import shared_task
from django.core.mail import send_mail
from .models import Artist

logger = logging.getLogger(__name__)

@shared_task
def send_congratulations_email(artist_id, album_name):
    try:
        artist = Artist.objects.get(id=artist_id)
        logger.info(f'Sending email to amar.link8@gmail.com for album: {album_name}')
        
        send_mail(
            'Congratulations on Your New Album!',
            f'Hi {artist.artist_name},\n\nCongratulations on releasing your new album: {album_name}!',
            'musicplatform@gmail.com',  # Your Gmail address or other email
            ['amar.link8@gmail.com'],  # Send to your specified email address
            fail_silently=False,
        )
        logger.info('Email sent successfully.')
    except Artist.DoesNotExist:
        logger.error(f'Artist with ID {artist_id} does not exist.')
    except Exception as e:
        logger.error(f'Error sending email: {str(e)}')


    @shared_task
    def my_daily_task():
        logger.info("Running daily task...")
        # Add your task logic here