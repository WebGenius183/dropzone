from django.contrib import admin
from .models import Genre, Movie, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
