from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from _bases.helpers import random_name
from _bases.models import BaseAddModify


class Comment(BaseAddModify):
    slug = models.SlugField(
        _('Slug'), max_length=10, unique=True, blank=True)
    text = models.CharField(
        _('Comment'), max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{str(self.added_by.username)} - {self.text}'

    def save(self, *args, **kwargs):
        self.slug = slugify(random_name(10))
        super().save(*args, **kwargs)


class MovieComment(Comment):
    movie = models.ForeignKey(
        'movies.Movie', on_delete=models.CASCADE,
        related_name='comments', verbose_name=_('Movie'))

    class Meta:
        verbose_name = _('Movie omment')
        verbose_name_plural = _('Movie Comments')

    def get_absolute_url(self):
        return reverse('moviecomment_detail', args=[self.slug])


class CelebComment(Comment):
    celeb = models.ForeignKey(
        'celebs.Celebrity', on_delete=models.CASCADE,
        related_name='comments', verbose_name=_('Celebrity'))

    class Meta:
        verbose_name = _('Celebrity Comment')
        verbose_name_plural = _('Celebrity Comments')

    def get_absolute_url(self):
        return reverse('celebcomment_detail', args=[self.slug])
