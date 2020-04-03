from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    GroupViewSet, UserViewSet,
    FavoriteCelebViewSet, UserFavoriteCelebViewSet,
    FavoriteGenreViewSet, UserFavoriteGenreViewSet,
    FavoriteMovieViewSet)


router = DefaultRouter()
router.register('group', GroupViewSet)
router.register('user', UserViewSet)
router.register('user_celeb', FavoriteMovieViewSet)
router.register('user_genre', FavoriteGenreViewSet)
router.register('user_movie', FavoriteMovieViewSet)

user_celebs = UserFavoriteCelebViewSet.as_view({
    'get': 'list'
})
user_genres = UserFavoriteGenreViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('user/<int:pk>/celebs/', user_celebs),
    path('user/<int:pk>/genres/', user_genres),
    path('', include(router.urls)),
]
