from rest_framework import serializers
from .models import Album, Song
from artists.models import Artist

class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # Allow passing id for updates
    image = serializers.ImageField(required=False, allow_null=True)
    audio_file = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Song
        fields = ['id', 'name', 'image', 'audio_file', 'album']
        extra_kwargs = {'album': {'required': False}}  # Make album optional in the serializer

class AlbumSerializer(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(required=False, help_text="Approve the album if its name is not explicit")
    songs = SongSerializer(many=True, required=True)
    artist_name = serializers.CharField(source='artist.artist_name', read_only=True)  # Read-only field

    class Meta:
        model = Album
        fields = ["id", "artist_name", "album_name", "release_datetime", "cost", "is_approved", "songs"]
        
    def perform_create(self, serializer):
        # This method is called when creating an album
        serializer.save(artist=self.request.user.artist)  # Associate the album with the artist

    def create(self, validated_data):
        songs_data = validated_data.pop('songs')

        # Get the artist from the request
        artist = self.context['request'].user.artist

        if not artist:
            raise serializers.ValidationError("User must have an associated artist.")

        # Create the album and associate it with the artist
        album = Album.objects.create(artist=artist, **validated_data)

        # Create associated songs
        for song_data in songs_data:
            Song.objects.create(album=album, **song_data)

        return album