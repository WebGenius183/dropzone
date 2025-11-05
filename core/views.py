from django.shortcuts import render, get_object_or_404
from . import models


def home(request):
    movie = models.Movie.objects.all()[:6]
    trending = models.Movie.objects.filter(trending=True)[:6]
    staff_pick = models.Movie.objects.filter(staff_pick=True)[:6]

    context = {
        'movie' : movie,
        'trending' : trending,
        'staff_pick' : staff_pick
    }
    return render(request, 'index.html', context)

def movie_list(request):
    movie = models.Movie.objects.all()
    context = {
        'movie' : movie
    }
    return render(request, 'movie_list.html', context)

def genre_list(request):
    genres = models.Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'genre_list.html', context)

def movie_detail(request, movie_id):
    movie = models.Movie.objects.get(id=movie_id)
    episode = models.Episode.objects.filter(movie=movie)
    related_movies = models.Movie.objects.filter(genre__in=movie.genre.all()).exclude(id=movie_id)[:6]
    context = {
        'movie': movie,
        'related': related_movies,
        'episode': episode
    }
    return render(request, 'movie_detail.html', context)

def search(request):
    query = request.GET.get('q', '')
    movies = models.Movie.objects.filter(title__icontains=query) if query else []

    return render(request, 'search.html', {
        'movies': movies,
        'query': query
    })

def genre_movies(request, id):
    genre = get_object_or_404(models.Genre, id=id)
    movies = models.Movie.objects.filter(genre=genre)

    return render(request, "genre.html", {
        'genre': genre,
        'movies': movies
    })

def page_not_found_custom(request, exception):
    return render(request, "404.html", status=404)
