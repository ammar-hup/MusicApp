import pytest
from ..models import *
from ..serializers import *

@pytest.mark.django_db
class TestArtists:
    def test_creation_faild(self):
        artist = ArtistSerializer(data={})
        assert artist.is_valid() == False

    def test_creation_sucsses(self):
        artist = Artist()
        artist.artist_name = "Anas"
        artist.social_link = "www.instgram.com/anashagras"
        artist.save()
        assert Artist.objects.count() == 1