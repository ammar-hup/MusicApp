from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='knox_register'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
]
