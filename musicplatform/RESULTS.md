# import the models first
from artists.models import Artist
from albums.models import Album

# Create
Artist.objects.create(name = "Drake" , socialLink = "https://www.instagram.com/drake/")

<Artist: Drake>

Artist.objects.create(name = "adle" , socialLink = "https://www.instagram.com/adle/")

<Artist: adle>

# Get All
Artist.objects.all()

<QuerySet [<Artist: Drake>, <Artist: adle>]>

# order_by
Artist.objects.all().order_by('-name')

<QuerySet [<Artist: Drake>, <Artist: adle>]>

# startswith
Artist.objects.filter(name__startswith='a')

<QuerySet [<Artist: adle>]>
# create artist and album

artist = Artist.objects.create(name = 'Ammar') 

album1 = Album.objects.create(name='Album 1', cost=9.99, artist=artist)  

Artist.objects.all() 

<QuerySet [<Artist: Ammar>]>.

Album.objects.all()  

<QuerySet [<Album: Album 1>]>

