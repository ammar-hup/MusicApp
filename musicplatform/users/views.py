from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.exceptions import NotFound
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Get the user by primary key (pk) or return 404
        obj = get_object_or_404(User, pk=self.kwargs['pk'])
        return obj

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = self.get_object()

        # Check if the user is the same as the one making the request
        if request.user != user:
            return Response({'detail': 'Not authorized to update this user.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(user, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        # Check if the user is the same as the one making the request
        if request.user != user:
            return Response({'detail': 'Not authorized to update this user.'}, status=status.HTTP_403_FORBIDDEN)
        
        # Partial update
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

        