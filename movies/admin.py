from django.contrib import admin

from _bases.admin import BaseAdmin
from .models import Genre, PgRating, Movie, MovieCrew


class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    autocomplete_fields = ('crew',)


@admin.register(Genre)
class GenreAdmin(BaseAdmin):
    search_fields = ('name',)


@admin.register(PgRating)
class PgRatingAdmin(BaseAdmin):
    search_fields = ('name',)

    list_display = ('name', 'code')


@admin.register(Movie)
class MovieAdmin(BaseAdmin):
    inlines = (MovieCrewInline,)

    list_display = ('name', 'release_year', 'imdb_rating',
                    'duration', 'pg_rating')
    autocomplete_fields = ('genres',)
