from rest_framework import status,generics,permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.exceptions import NotFound
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LogoutView ,LoginView
from .serializers import *
from .models import *

   
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response({
            "user": RegisterSerializer(user).data,
            "token": token
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = serializer.validated_data['token']
        user_data = {
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'bio': user['bio']
        }
        return Response({
            'token': token,
            'user': user_data
        }, status=status.HTTP_200_OK)

class LogoutView(LogoutView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Invalidate the token for the current user
        request._auth.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_204_NO_CONTENT)