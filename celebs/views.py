from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .forms import CommentForm
from .models import Celebrity


# vue views
class DutyList(TemplateView):
    template_name = 'vue/celebs/duty_list.html'


class DutyDetail(TemplateView):
    template_name = 'vue/celebs/duty_detail.html'


class CelebrityList(TemplateView):
    template_name = 'vue/celebs/celeb_list.html'


class CelebrityDetail(TemplateView):
    template_name = 'vue/celebs/celeb_detail.html'


# html views
pagination = 10


class HtmlCelebrityList(ListView):
    template_name = 'html/celebs/celeb_list.html'
    queryset = Celebrity.objects.prefetch_related(
        'moviecrews__duty', 'moviecrews__movie', 'comments')
    context_object_name = 'celebs'
    paginate_by = pagination


class HtmlCelebrityDetail(SuccessMessageMixin, DetailView, CreateView):
    template_name = 'html/celebs/celeb_detail.html'
    queryset = Celebrity.objects.prefetch_related(
        'moviecrews__duty', 'moviecrews__movie', 'comments')
    form_class = CommentForm
    success_message = _('Your comment has been sent succesfully!')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse(
            'html_celeb_detail',
            kwargs={
                'slug': self.object.celeb.slug
            }
        )
