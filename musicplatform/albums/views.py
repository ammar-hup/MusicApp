from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def index(request):
    return HttpResponse("You're at the Album index.")

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album_name = form.cleaned_data['album_name']
            cost = form.cleaned_data['cost']
            artist = form.cleaned_data['artist']
            is_approved = form.cleaned_data['is_approved']

            # Do something with the retrieved data (e.g., create an Album instance)
            new_album = Album.objects.create(
                album_name=album_name,
                cost=cost,
                artist=artist,
                is_approved=is_approved,
            )
            return redirect(request.path)  # Redirect to the artist list view or any other desired page after successful form submission
    else:
        form = AlbumForm()

    return render(request, 'albums/create_album.html', {'form': form})
    