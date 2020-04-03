from unidecode import unidecode

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from _bases.models import BaseAddModify, BaseNameSlug
from _bases.helpers import random_name, video_code, age


def celeb_directory_path(instance, filename):
    return f'celebs/{instance.id}_{filename.lower()}_{random_name(5)}'


class Duty(BaseAddModify, BaseNameSlug):
    """Duty of Celebs"""
    code = models.CharField(
        _('Code'), max_length=1)

    class Meta:
        verbose_name = _('Duty')
        verbose_name_plural = _('Duties')
        ordering = ('code',)

    def get_absolute_url(self):
        return reverse('duty_detail', args=[self.slug])


class Celebrity(BaseAddModify):
    """Celebrity model"""
    slug = models.SlugField(
        _('Slug'), max_length=160, unique=True, blank=True)

    first_name = models.CharField(
        _('First Name'), max_length=75)
    last_name = models.CharField(
        _('Last Name'), max_length=75)
    nick_name = models.CharField(
        _('Nick Name'), max_length=50, default='', blank=True)

    birth_date = models.DateField(
        _('Birth Date'), blank=True, null=True)
    birth_place = models.CharField(
        _('Birth Place'), max_length=100, default='', blank=True)

    content = models.TextField(
        _('Biography'), default='', blank=True)
    source_content = models.URLField(  # credits
        _('Biography Souce'), default='', blank=True)
    trailer = models.URLField(
        _('Trailer'), default='', blank=True,
        help_text=_('trailer url (ONLY for youtube videos yet)'))

    image = models.ImageField(
        _('Image'),
        default='celebs/default_celeb.jpg', upload_to=celeb_directory_path,
        blank=True, null=True)
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(250, 400)],
        format='JPEG', options={'quality': 80})
    credit_image = models.CharField(  # credits
        _('Image Credit'), max_length=250, default='', blank=True)

    duties = models.ManyToManyField(
        Duty, related_name='celebs', verbose_name=_('Duties'),
        help_text=_("Celebrities' duties in movies"))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return age(self.birth_date)

    @property
    def as_cast(self):
        return self._get_movie('C')

    @property
    def as_director(self):
        return self._get_movie('D')

    @property
    def as_producer(self):
        return self._get_movie('P')

    @property
    def as_writer(self):
        return self._get_movie('W')

    @property
    def youtube_video(self):
        return video_code(self.trailer)

    class Meta:
        verbose_name = _('Celebrity')
        verbose_name_plural = _('Celebrities')
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(unidecode(self.first_name + ' ' + self.last_name))
            self.slug = slug + '-' + random_name(5)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('celeb_detail', args=[self.slug])

    def _get_movie(self, duty_code):
        if hasattr(self, '_prefetched_objects_cache') and 'moviecrews' in self._prefetched_objects_cache:
            return [c for c in self._prefetched_objects_cache['moviecrews'] if c.duty.code == duty_code]
        else:
            return self.moviecrews.filter(duty__code=duty_code)


# EXPLICITLY DEFINED MTM MODELS
class CelebrityDuty(models.Model):
    celeb = models.ForeignKey(
        Celebrity, on_delete=models.CASCADE,
        related_name='celebduties', verbose_name=_('Celebrity'))
    duty = models.ForeignKey(
        Duty, on_delete=models.CASCADE,
        related_name='celebduties', verbose_name=_('Duty'))

    class Meta:
        verbose_name = _('Celebrity Duty')
        verbose_name_plural = _('Celebrity Duties')
