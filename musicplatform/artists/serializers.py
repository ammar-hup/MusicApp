from rest_framework import serializers
from .models import *
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','artist_name','social_link']

    def validate_stage_name(self, value):
        if Artist.objects.filter(artist_name=value).exists():
            raise serializers.ValidationError("This artist name already exists.")
        return value

    def validate(self, data):
        if not data.get('artist_name'):
            raise serializers.ValidationError("Artist name is required.")
        return data