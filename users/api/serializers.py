from rest_framework import serializers

from users.models import (
    User, Group, FavoriteGenre, FavoriteMovie, FavoriteCeleb)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email',
            'is_staff', 'is_active')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class FavoriteGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteGenre
        fields = ('id', 'user', 'genre')


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ('id', 'user', 'movie', 'note', 'is_watched', 'watch_list')


class FavoriteCelebSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCeleb
        fields = ('id', 'user', 'celeb')
