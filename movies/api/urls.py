from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    GenreViewSet, PgRatingViewSet, MovieViewSet,
    MovieGenreViewSet, MovieCrewViewSet,
    GenreMovieViewSet)

router = DefaultRouter()
router.register('genre', GenreViewSet)
router.register('pg_rating', PgRatingViewSet)
router.register('movie', MovieViewSet)

genre_movies = GenreMovieViewSet.as_view({
    'get': 'list'
})

movie_genres = MovieGenreViewSet.as_view({
    'get': 'list'
})
movie_crews = MovieCrewViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('genre/<slug:slug>/movies/', genre_movies),
    path('movie/<slug:slug>/genres/', movie_genres),
    path('movie/<slug:slug>/crews/', movie_crews),
    path('', include(router.urls))
]
