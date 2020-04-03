from rest_framework import viewsets
from rest_framework.response import Response

from movies.models import Genre, PgRating, Movie, MovieCrew
from .serializers import (
    GenreSerializer, MovieSerializer, MovieCrewSerializer, PgRatingSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'


class PgRatingViewSet(viewsets.ModelViewSet):
    queryset = PgRating.objects.all()
    serializer_class = PgRatingSerializer
    lookup_field = 'slug'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related('genres', 'crews', 'pg_rating')
    serializer_class = MovieSerializer
    lookup_field = 'slug'


class GenreMovieViewSet(viewsets.ViewSet):
    """the movies of each genre"""

    def list(self, request, slug=None):
        queryset = Movie.objects.prefetch_related(
            'genres', 'crews', 'pg_rating').filter(genres__slug=slug)
        serializer = MovieSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class MovieGenreViewSet(viewsets.ViewSet):
    """the genres of each movie"""
    # permission_classes =

    def list(self, request, slug=None):
        queryset = Genre.objects.prefetch_related(
            'movies').filter(movies__slug=slug)
        serializer = GenreSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class MovieCrewViewSet(viewsets.ViewSet):
    # permission_classes =

    def list(self, request, slug=None):
        queryset = MovieCrew.objects.select_related(
            'movie', 'crew').filter(movie__slug=slug)
        serializer = MovieCrewSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
