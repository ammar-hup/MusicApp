# import the models first
from artists.models import Artist
from albums.models import Album

# Create
Artist.objects.create(artist_name = "Drake" , social_link = "https://www.instagram.com/drake/")

<Artist: Drake>

Artist.objects.create(artist_name = "adle" , social_link = "https://www.instagram.com/adle/")

<Artist: adle>

# Get All
Artist.objects.all()

<QuerySet [<Artist: Drake>, <Artist: adle>]>

# order_by
Artist.objects.all().order_by('-artist_name')

<QuerySet [<Artist: Drake>, <Artist: adle>]>

# startswith
Artist.objects.filter(artist_name__startswith='a')

<QuerySet [<Artist: adle>]>
# create artist and album

artist = Artist.objects.create(artist_name = 'Ammar') 

album1 = Album.objects.create(album_name='Album 1', cost=9.99, artist=artist)  

Artist.objects.all() 

<QuerySet [<Artist: Ammar>]>.

Album.objects.all()  

<QuerySet [<Album: Album 1>]>

Album.objects.all().order_by('-release_datetime')

<QuerySet [<Album: Album 3>, <Album: Album 1>]>

today = timezone.now().date()

Album.objects.filter(release_datetime__lte=today) 

Album.objects.count()

2

-----------------------
from myapp.models import Artist, Album

artists = Artist.objects.all()
for artist in artists:
    print(f"Artist: {artist.artist_name}")
    albums = Album.objects.filter(artist=artist)
    for album in albums:
        print(f" - Album: {album.album_name}")


Artist: Ammar
Artist: ahmed
 - Album: Album 1
Artist: drake
 - Album: Album 3

-------------------------------

Album.objects.all().order_by('cost')

<QuerySet [<Album: Album 3>, <Album: Album 1>]>

-----------------------------------

Album.objects.all().order_by('artist_name')

<QuerySet [<Album: Album 1>, <Album: Album 3>]>

-----------------------------------

 Artist.objects.annotate(approved_albums=Count('album',filter=Q(album__is_approved=True))).order_by('approved_albums')

 <QuerySet [<Artist: drake>, <Artist: Ammar>, <Artist: ahmed>]>




 <!-- {% block content %}
  {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  {% if next %}
    {% if user.is_authenticated %}
      <p>Your account doesn't have access to this page. To proceed,
      please login with an account that has access.</p>
    {% else %}
      <p>Please login to see this page.</p>
    {% endif %}
  {% endif %}

  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
      <tr>
        <td>{{ form.username.label_tag }}</td>
        <td>{{ form.username }}</td>
      </tr>
      <tr>
        <td>{{ form.password.label_tag }}</td>
        <td>{{ form.password }}</td>
      </tr>
    </table>
    <input type="submit" value="login">
    <input type="hidden" name="next" value="{{ next }}">
  </form>

  {# Assumes you set up the password_reset view in your URLconf #}
  <p><a href="{% url 'password_reset' %}">Lost password?</a></p>

{% endblock %} -->

