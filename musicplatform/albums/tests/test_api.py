import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import *
from artists.models import *
from artists.serializers import *
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile

pytestmark = pytest.mark.django_db

class TestAlbumAPI:
    def test_get(self):
        client = APIClient()
        response = client.get(reverse('album-create'))
        assert response.status_code == 200

    def test_post_with_wrong_data(self):
        client = APIClient()
        artist_data = {"artist_name": "TestName", "socialLink": "https://www.instagram.com/"}
        artist = ArtistSerializer(data=artist_data)
        if artist.is_valid():
            artist_instance = artist.save()  # Save the artist instance
        else:
            print(artist.errors)  # Print errors if artist is not valid

        response = client.post(reverse('album-create'),
                                {
                                    "album_name": "my album"
                                },
                                format='json'
                                )
        assert response.status_code == 400

    def test_post_with_correct_data(self):
        client = APIClient()
        
        # Create an artist
        artist_data = {"artist_name": "TestName", "socialLink": "https://www.instagram.com/"}
        artist = ArtistSerializer(data=artist_data)
        if artist.is_valid():
            artist_instance = artist.save()  # Save the artist instance
        else:
            print(artist.errors)  # Print errors if artist is not valid

        # Create the album with at least one song
        response = client.post(reverse('album-create'),
                                {
                                    "album_name": "my album",
                                    "artist": artist_instance.id,  # Use the saved artist's ID
                                    'cost': 200,
                                    'releaseDateTime': datetime.now().isoformat(),  # Use ISO format
                                    "songs": [
                                        {
                                            "name": "Song 1",
                                            "audio_file": None,  # Set to None if you don't want to send files
                                            "image": None  # Set to None if you don't want to send files
                                        }
                                    ]
                                },
                                format='json'
                                )
        
        print(response.data)  # Output the response data for debugging
        assert response.status_code == 201, f"Album creation failed: {response.data}"