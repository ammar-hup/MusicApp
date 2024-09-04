from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # API routes
    path('', views.ArtistViewList.as_view(), name='artist-list'),
    path('<int:pk>/', views.RetrieveUpdateDestroyArtistView.as_view(), name='artist-update_delete'),
    path('api-token-auth',obtain_auth_token),
    path('api/', include('rest_framework.urls', namespace='api')),
    # Web routes
    path('create/', views.ArtistViewCreate.as_view(), name='artist-create'),
]