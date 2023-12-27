from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect ,HttpResponse
from .models import Artist,ArtistManager
from .forms import ArtistForm

# Create your views here.

def artist_list(request):
    # Fetch artists and their related albums in one query
    artists = Artist.objects.prefetch_related('album_set').all()
    return render(request, 'artists/artist_list.html', {'artists': artists})

# create artist from the form
def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['artist_name']
            Artist.objects.create(artist_name=name)
            return redirect(request.path)  # Redirect to the artist list view or any other desired page after successful form submission
    else:
        form = ArtistForm()

    return render(request, 'artists/create_artist.html', {'form': form})
