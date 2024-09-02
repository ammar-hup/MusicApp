import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from albums.models import Album, Song
from artists.models import Artist

@pytest.mark.django_db
class TestSongModel:

    @pytest.fixture
    def artist(self):
        return Artist.objects.create(artist_name="Test Artist")

    @pytest.fixture
    def album(self, artist):
        return Album.objects.create(album_name="Test Album", cost=9.99, artist=artist)

    @pytest.fixture
    def song(self, album):
        return Song.objects.create(
            name="Test Song",
            album=album,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
            audio_file=SimpleUploadedFile("test_audio.mp3", b"file_content", content_type="audio/mpeg")
        )

    def test_song_creation(self, song):
        assert song.name == "Test Song"
        assert song.album.album_name == "Test Album"
        assert song.image.name.startswith("songs/test_image")  # Check if it starts with the expected path
