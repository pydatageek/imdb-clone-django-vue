from django.urls import path

from .views import (
    GroupList, GroupDetail, UserList, UserDetail,
    FavoriteGenreList, FavoriteGenreDetail,
    FavoriteMovieList, FavoriteMovieDetail,
    FavoriteCelebList, FavoriteCelebDetail
)

urlpatterns = [
    # vue urls
    path('group/', GroupList.as_view(), name='group_list'),
    path('group/<int:pk>/', GroupDetail.as_view(), name='group_detail'),
    path('genre/', FavoriteGenreList.as_view(), name='user_genre_list'),
    path('genre/<int:pk>/', FavoriteGenreDetail.as_view(),
         name='user_genre_detail'),
    path('movie/', FavoriteMovieList.as_view(), name='user_movie_list'),
    path('movie/<int:pk>/', FavoriteMovieDetail.as_view(),
         name='user_movie_detail'),
    path('celeb/', FavoriteCelebList.as_view(), name='user_celeb_list'),
    path('celeb/<int:pk>/', FavoriteCelebDetail.as_view(),
         name='user_celeb_detail'),
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>/', UserDetail.as_view(), name='user_detail'),
]
