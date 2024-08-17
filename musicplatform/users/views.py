from rest_framework import status,generics,permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.exceptions import NotFound
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .serializers import *
from .models import *

   
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self):
        pk = self.kwargs['pk']
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail="User not found")

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return Response({'detail': 'Not authorized to update this user.'}, status=403)
        serializer = self.get_serializer(user, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return Response({'detail': 'Not authorized to update this user.'}, status=403)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()