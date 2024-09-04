from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(max_length=255, required=True)  # Set required=True
    class Meta:
        model = Artist
        fields = ['artist_name']  # Only include artist_name for creation
    
    def validate_artist_name(self, value):
        if Artist.objects.filter(artist_name=value).exists():
            raise serializers.ValidationError("This artist name already exists.")
        return value

    def validate_artist_name(self, value):
        # This check is not necessary if you're using get_or_create in AlbumSerializer
        if not value:
            raise serializers.ValidationError("Artist name is required.")
        return value