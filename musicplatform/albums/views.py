from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def index(request):
    return HttpResponse("You're at the Album index.")
# the form method
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album_name = form.cleaned_data['album_name']
            cost = form.cleaned_data['cost']
            artist = form.cleaned_data['artist']
            is_approved = form.cleaned_data['is_approved']

            # create an Album instance with the retrieved data
            new_album = Album.objects.create(
                album_name=album_name,
                cost=cost,
                artist=artist,
                is_approved=is_approved,
            )
            return redirect(request.path)  # Redirect to the same page after creating an album , and be able to create another album
    else:
        form = AlbumForm()

    return render(request, 'albums/create_album.html', {'form': form})
    