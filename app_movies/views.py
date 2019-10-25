from django.shortcuts import render, get_object_or_404
from .models import Movie


def details(request, id, slug):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "movies/details.html",{
        "movie": movie
    })
