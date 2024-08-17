from rest_framework import serializers,status
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from users.models import User
from django.contrib.auth import authenticate
from knox.models import AuthToken
from knox.auth import TokenAuthentication

# register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio']

    def validate(self, data):
        # Ensure passwords match
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        # Validate the strength of the password
        try:
            validate_password(data['password1'])
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'password1': list(e.messages)})

        return data
    
    def validate_email(self, value):
        # Store email domain in lowercase
        return value.lower()
    
    def create(self, validated_data):
        # Remove password1 and password2 from the validated data
        password = validated_data.pop('password1')
        validated_data.pop('password2')

        # Create the user and hash the password
        user = User.objects.create_user(**validated_data, password=password)
        return user

# login serializer
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        
        # Create token and return it along with user data
        token = AuthToken.objects.create(user=user)[1]
        return {
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'bio': user.bio
            }
        }
    
class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []
