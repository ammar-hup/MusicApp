from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'), 
    path('admin/', admin.site.urls),
    path('albums/', include('albums.urls')),
    path('artists/', include('artists.urls')),
    path('auth/', include('authentication.urls')),
    path('users/', include('users.urls')),
    path('api-auth/knox/', include('knox.urls')),  # Knox URLs
    path('api-auth/', include('rest_framework.urls')), #rest_framework.urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)