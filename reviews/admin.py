from django.contrib import admin

from _bases.admin import BaseAdmin
from .models import MovieComment, CelebComment


@admin.register(MovieComment)
class MovieCommentAdmin(BaseAdmin):
    pass


@admin.register(CelebComment)
class CelebCommentAdmin(BaseAdmin):
    pass
