from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'release_datetime', 'cost', 'artist', 'is_approved']
        exclude = ['release_datetime']

    widgets = {
        'release_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
        