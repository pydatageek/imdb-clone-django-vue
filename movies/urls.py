from django.urls import path

from .views import (
    GenreList, GenreDetail, PgRatingList, PgRatingDetail,
    MovieList, MovieDetail)

urlpatterns = [
    # vue urls
    path('genre/', GenreList.as_view(), name='genre_list'),
    path('genre/<slug:slug>/', GenreDetail.as_view(), name='genre_detail'),
    path('pg-rating/', PgRatingList.as_view(), name='pg_rating_list'),
    path('pg-rating/<slug:slug>/',
         PgRatingDetail.as_view(), name='pg_rating_detail'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('', MovieList.as_view(), name='movie_list'),
]
