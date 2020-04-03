from rest_framework import viewsets
from rest_framework.response import Response

from users.models import (
    Group, User, FavoriteGenre, FavoriteMovie, FavoriteCeleb)
from .serializers import (
    GroupSerializer, UserSerializer,
    FavoriteGenreSerializer, FavoriteMovieSerializer, FavoriteCelebSerializer)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FavoriteGenreViewSet(viewsets.ModelViewSet):
    queryset = FavoriteGenre.objects.select_related('user', 'genre')
    serializer_class = FavoriteGenreSerializer


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.select_related('user', 'movie')
    serializer_class = FavoriteMovieSerializer


class FavoriteCelebViewSet(viewsets.ModelViewSet):
    queryset = FavoriteCeleb.objects.select_related('user', 'celeb')
    serializer_class = FavoriteCelebSerializer


class UserFavoriteCelebViewSet(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = FavoriteCeleb.objects.select_related(
            'user', 'celeb').filter(user=pk)
        serializer = FavoriteCelebSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class UserFavoriteGenreViewSet(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = FavoriteGenre.objects.select_related(
            'user', 'genre').filter(user=pk)
        serializer = FavoriteGenreSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
