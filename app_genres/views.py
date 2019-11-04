from django.shortcuts import render, get_object_or_404
from app_movies.models import Movie
from .models import Genre

def listing(request, slug=None):
    genre = None
    search = None
    filters = {}
    genres = Genre.objects.all()
    if 'search' in request.GET and len(request.GET['search']) > 0:
        search = request.GET['search']
        filters['title__icontains'] = search
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        filters['genre'] = genre
    movies = Movie.objects.filter(**filters)
    return render(request, "genres/listing.html", {
        "genres": genres,
        "activeGenre": genre,
        "movies": movies,
        "search": search
    })
