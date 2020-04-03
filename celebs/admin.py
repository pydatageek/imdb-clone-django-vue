from django.contrib import admin

from _bases.admin import BaseAdmin
from .forms import CelebrityForm
from .models import Duty, Celebrity


@admin.register(Duty)
class DutyAdmin(BaseAdmin):
    pass


@admin.register(Celebrity)
class CelebrityAdmin(BaseAdmin):
    form = CelebrityForm

    list_filter = ('duties',)
    search_fields = ('first_name', 'last_name', 'duties__name')
