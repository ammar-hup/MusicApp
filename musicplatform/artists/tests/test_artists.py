import pytest
from ..models import *
from ..serializers import *

@pytest.mark.django_db
class TestArtists:
    def test_creation_fails_without_name(self):
        # Create an empty data dictionary
        data = {}
        
        # Initialize the serializer with empty data
        serializer = ArtistSerializer(data=data)
        
        # Check if the serializer is invalid (i.e., it has validation errors)
        assert not serializer.is_valid()
        
        # Get the validation errors
        errors = serializer.errors
        
        # Check if there are any validation errors related to missing artist name
        assert 'artist_name' in errors
        
        # Check if the error message indicates that artist name is required
        assert errors['artist_name'][0] == 'This field is required.'

    def test_creation_sucsses(self):
        artist = Artist()
        artist.artist_name = "Anas"
        artist.social_link = "www.instgram.com/anashagras"
        artist.save()
        assert Artist.objects.count() == 1