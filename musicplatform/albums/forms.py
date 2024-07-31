from django import forms
from .models import Album, Song
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, inlineformset_factory

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
class SongForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    audioFile = forms.FileField(required=True)
    class Meta:
        model = Song
        fields = '__all__'    
