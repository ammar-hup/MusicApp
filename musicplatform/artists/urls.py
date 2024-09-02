from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # API routes
    path('', views.ArtistList.as_view(), name='artist-list'),
    path('api-token-auth',obtain_auth_token),
    path('api-auth', include('rest_framework.urls')),
    # Web routes
    path('create/', views.ArtistCreateView.as_view(), name='artist-create'),
]