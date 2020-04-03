"""Project-wide base models inherited by other models"""
from unidecode import unidecode

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from crum import get_current_user


# BASE MODELS
class BaseAddModify(models.Model):
    """Base model for Added and Modified Dates and Users fields"""
    added_date = models.DateTimeField(
        _('Added Date'), auto_now_add=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='%(app_label)s_%(class)s_adders', verbose_name=_('Added By'))

    modified_date = models.DateTimeField(
        _('Added Date'), auto_now=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='%(app_label)s_%(class)s_modifiers', verbose_name=_('Modified By'))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.added_by = user

        self.modified_by = user
        super().save(*args, **kwargs)


class BaseNameSlug(models.Model):
    """Base model for name and slug fields"""
    name = models.CharField(
        _('Name'), max_length=100, unique=True)
    slug = models.SlugField(
        _('Slug'), max_length=110, unique=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
