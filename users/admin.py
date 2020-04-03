from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BUserAdmin, GroupAdmin as BGroupAdmin)

from .models import (
    User, Group, BGroup,
    FavoriteGenre, FavoriteMovie, FavoriteCeleb)

admin.site.unregister(BGroup)


@admin.register(User)
class UserAdmin(BUserAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BGroupAdmin):
    pass


@admin.register(FavoriteGenre)
class FavoriteGenreAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteCeleb)
class FavoriteCelebAdmin(admin.ModelAdmin):
    pass
