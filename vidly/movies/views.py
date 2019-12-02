from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie


def index(request):
    movie = Movie.objects.all();
    return render(request, 'movies/index.html', {'movies': movie})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id);
    return render(request, 'movies/details.html', { 'movie': movie });