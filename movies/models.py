"""
models related with Movies
e.g. Movie, Genre
"""
from unidecode import unidecode

from django.conf import settings
from django.core.validators import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from crum import get_current_user
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from _bases.helpers import random_name, video_code
from _bases.models import BaseAddModify, BaseNameSlug


def movie_directory_path(instance, filename):
    return f'movies/{instance.id}_{filename.lower()}_{random_name(5)}'


# MOVIE RELATED MODELS
class Genre(BaseAddModify, BaseNameSlug):
    """Genres of movies"""
    content = models.CharField(
        _('Content'), max_length=250, default='', blank=True)

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('genre_detail', args=[self.slug])


class PgRating(BaseAddModify, BaseNameSlug):
    """Genres of movies"""
    code = models.CharField(
        _('Code'), max_length=5)
    content = models.CharField(
        _('Content'), max_length=250, default='', blank=True)

    class Meta:
        verbose_name = _('PG Rating')
        verbose_name_plural = _('PG Ratings')
        ordering = ('pk',)

    def __str__(self):
        return f'{self.code} ({self.name})'

    def get_absolute_url(self):
        return reverse('pgrating_detail', args=[self.slug])


class Movie(BaseAddModify, BaseNameSlug):
    """Movie model"""
    name = models.CharField(
        _('Name'), max_length=100)
    slug = models.SlugField(
        _('Slug'), max_length=110, unique=True, blank=True)

    release_year = models.CharField(
        _('Release Year'), max_length=4)
    duration = models.SmallIntegerField(
        _('Duration'), default=0, blank=True, help_text=_('in minutes'))
    imdb_rating = models.FloatField(
        _('IMDB Rating'), default=0, blank=True,
        help_text=_('e.g. 6.8'))

    content = models.TextField(
        _('Content'), default='', blank=True)
    source_content = models.URLField(  # credits
        _('Content Source'), default='', blank=True)
    trailer = models.URLField(
        _('Trailer'), default='', blank=True,
        help_text=_('trailer url (ONLY for youtube videos yet)'))

    image = models.ImageField(
        _('Image'),
        default='movies/default-movie.jpg', upload_to=movie_directory_path,
        blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(250, 400)],
        format='JPEG', options={'quality': 80})
    credit_image = models.CharField(  # credits
        _('Image Credit'), max_length=250, default='', blank=True)

    pg_rating = models.ForeignKey(
        PgRating, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='movies', verbose_name=_('PG Rating'))

    genres = models.ManyToManyField(
        Genre, related_name='movies', verbose_name=_('Genres'))

    crews = models.ManyToManyField(
        'celebs.Celebrity', through='MovieCrew',
        related_name='movies', verbose_name=_('Crews'))

    @property
    def casts(self):
        return self._get_crew('C')

    @property
    def directors(self):
        return self._get_crew('D')

    @property
    def producers(self):
        return self._get_crew('P')

    @property
    def writers(self):
        return self._get_crew('W')

    @property
    def youtube_video(self):
        return video_code(self.trailer)

    class Meta:
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
        ordering = ('-release_year', 'name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name) + '-' + random_name(5))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('movie_detail', args=[self.slug])

    def _get_crew(self, duty_code):
        if hasattr(self, '_prefetched_objects_cache') and 'moviecrews' in self._prefetched_objects_cache:
            return [c for c in self._prefetched_objects_cache['moviecrews'] if c.duty.code == duty_code]
        else:
            return self.moviecrews.filter(duty__code=duty_code)


# EXPLICITLY DEFINED MTM MODELS
# class MovieGenre(models.Model):
#     movie = models.ForeignKey(
#         Movie, on_delete=models.CASCADE,
#         related_name='moviegenres', verbose_name=_('Movie'))
#     genre = models.ForeignKey(
#         Genre, on_delete=models.CASCADE,
#         related_name='moviegenres', verbose_name=_('Genre'))

#     class Meta:
#         verbose_name = _('Movie Genre')
#         verbose_name_plural = _('Movie Genres')


class MovieCrew(models.Model):
    duty = models.ForeignKey(
        'celebs.Duty', on_delete=models.CASCADE, default=1,  # default is Cast
        related_name='moviecrews', verbose_name=_('Duty'))

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name='moviecrews', verbose_name=_('Movie'))
    crew = models.ForeignKey(
        'celebs.Celebrity', on_delete=models.CASCADE,
        related_name="moviecrews", verbose_name=_('Crew'))

    role = models.CharField(
        _('Role'), max_length=75, default='', blank=True,
        help_text=_('e.g. short story, screenplay for writer or voice for cast'))
    screen_name = models.CharField(
        _('Screen Name'), max_length=75, default='', blank=True,
        help_text=_("Crew's name on movie"))

    def clean(self, *args, **kwargs):
        if not self.duty in self.crew.duties.all():
            raise ValidationError(
                _('Crew duty and selected duty should match'), code='invalid')
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.crew.full_name
