from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import *
from django import forms

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class UserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),
    )

admin.site.register(User, UserAdmin)