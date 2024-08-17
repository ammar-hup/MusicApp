from rest_framework import status,generics,permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.exceptions import NotFound
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .serializers import *
from .models import *

   
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
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

class LogoutView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def get(self, request, *args, **kwargs):
        return Response({"detail": "Method \"GET\" not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        request.auth.delete()  # Delete the token to log out the user
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_204_NO_CONTENT)