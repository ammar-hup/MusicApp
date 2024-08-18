from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', UserListAPIView.as_view(), name='users-list'),  # listing all users

]
