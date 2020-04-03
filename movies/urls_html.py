from django.urls import path

from .views import (
    HtmlGenreList, HtmlGenreMovieList,
    HtmlMovieList, HtmlMovieDetail, HtmlTopMovieList
)

urlpatterns = [
    # html urls
    path('top/', HtmlTopMovieList.as_view(), name='html_top_movie_list'),
    path('genre/<slug:slug>/', HtmlGenreMovieList.as_view(),
         name='html_movie_by_genre'),
    path('genre/', HtmlGenreList.as_view(), name='html_genre_list'),
    path('<slug:slug>/', HtmlMovieDetail.as_view(),
         name='html_movie_detail'),
    path('', HtmlMovieList.as_view(), name='html_movie_list'),
]
