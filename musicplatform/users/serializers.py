from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate ,login

# user serializer
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']
        extra_kwargs = {
            'bio': {'required': False},
            'username': {'required': False},
            'email': {'required': False},
        }

    def update(self, instance, validated_data):
        # Update fields only if they are present in the request
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance