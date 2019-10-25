from django.shortcuts import render, get_object_or_404
from app_movies.models import Movie
from .models import Genre


def listing(request, slug=None):
    genre = None
    filters = {}
    genres = Genre.objects.all()
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        filters['genre'] = genre
    movies = Movie.objects.filter(**filters)
    
    return render(request, "genres/listing.html", {
        "genres": genres,
        "slug": slug,
        "movies": movies
    })
