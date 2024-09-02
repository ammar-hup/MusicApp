from rest_framework import serializers
from .models import Album, Song

class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # Allow passing id for updates
    image = serializers.ImageField(required=False, allow_null=True)
    audio_file = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Song
        fields = ['id', 'name', 'image', 'audio_file', 'album']
        extra_kwargs = {'album': {'required': False}}  # Make album optional in the serializer

class AlbumSerializer(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")
    songs = SongSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        songs_data = validated_data.pop('songs', [])
        album = Album.objects.create(**validated_data)
        for song_data in songs_data:
            Song.objects.create(album=album, **song_data)
        return album

    def update(self, instance, validated_data):
        songs_data = validated_data.pop('songs', [])
        # Update Album fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update or create songs
        existing_songs = {song.id: song for song in instance.songs.all()}
        song_ids_in_data = set()
        for song_data in songs_data:
            song_id = song_data.get('id')
            if song_id and song_id in existing_songs:
                # Update existing song
                song = existing_songs[song_id]
                for attr, value in song_data.items():
                    if attr != 'album':  # Skip setting album as it's already correct
                        setattr(song, attr, value)
                song.save()
                song_ids_in_data.add(song_id)
            else:
                # Create new song
                Song.objects.create(album=instance, **song_data)

        # Delete songs that are not in the update data
        for song_id, song in existing_songs.items():
            if song_id not in song_ids_in_data:
                song.delete()

        return instance

    def validate(self, data):
        if self.instance is None:  # Only for creation
            if not data.get('songs'):
                raise serializers.ValidationError("An album must have at least one song.")
        return data