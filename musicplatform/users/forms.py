from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'bio')  # Specify fields as needed
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
