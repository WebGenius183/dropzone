from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = "core.views.page_not_found_custom"

urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.movie_list, name="movie_list"),
    path("genres/", views.genre_list, name="genre_list"),
    path("genre/<int:id>/", views.genre_movies, name="genre_movies"),
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("search/", views.search, name="search"),
]
