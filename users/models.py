from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group as BGroup
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from crum import get_current_user
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from _bases.helpers import random_name


def user_directory_path(instance, filename):
    return f'users/{instance.id}_{filename.lower()}_{random_name(5)}'


class User(AbstractUser):
    email = models.EmailField(_('Email'), unique=True)

    genres = models.ManyToManyField(
        'movies.Genre', related_name='users', verbose_name=_('Genres'))
    movies = models.ManyToManyField(
        'movies.Movie', through='FavoriteMovie',
        related_name='users', verbose_name=_('Movies'))

    image = models.ImageField(
        _('Image'),
        default='users/default-user.jpg', upload_to=user_directory_path,
        blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(80, 80)],
        format='JPEG', options={'quality': 80})


class Group(BGroup):
    pass


# EXPLICITLY DEFINED MTM MODELS
# Below Models are not active for now!
class FavoriteCeleb(models.Model):
    """Users' favorite celebs"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='favoritecelebs', verbose_name=_('User'))
    celeb = models.ForeignKey(
        'celebs.Celebrity', on_delete=models.CASCADE,
        related_name='favoritecelebs', verbose_name=_('Celebrity'))

    class Meta:
        verbose_name = _('Favorite Celebrity')
        verbose_name_plural = _('Favorite Celebrities')
        unique_together = ('user', 'celeb')

    def __str__(self):
        return f'{self.user.username} - {self.celeb.full_name}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('user_celeb_detail', args=['pk'])

    # def save(self, *args, **kwargs):
    #     user = get_current_user()
    #     if user and not user.pk:
    #         user = None
    #     self.user = user
    #     super().save(*args, **kwargs)


class FavoriteGenre(models.Model):
    """Users' favorite genres"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='favoritegenres', verbose_name=_('User'))
    genre = models.ForeignKey(
        'movies.Genre', on_delete=models.CASCADE,
        related_name='favoritegenres', verbose_name=_('Genre'))

    class Meta:
        verbose_name = _('Favorite Genre')
        verbose_name_plural = _('Favorite Genres')
        unique_together = ('user', 'genre')

    def __str__(self):
        return f'{self.user.username} - {self.genre.name}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('user_genre_detail', args=['pk'])


class FavoriteMovie(models.Model):
    """Users' favorite movies"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='favoritemovies', verbose_name=_('User'))
    movie = models.ForeignKey(
        'movies.Movie', on_delete=models.CASCADE,
        related_name='favoritemovies', verbose_name=_('Movie'))

    note = models.CharField(
        _('Note'), max_length=250, default='', blank=True,
        help_text=_('User note about movie'))
    is_watched = models.BooleanField(
        default=False, verbose_name='Have you watched?')
    watch_list = models.BooleanField(
        default=False, verbose_name='Add to Watch List?')

    class Meta:
        verbose_name = _('Favorite Movie')
        verbose_name_plural = _('Favorite Movies')
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user.username} - {self.movie.name}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('user_movie_detail', args=['pk'])
