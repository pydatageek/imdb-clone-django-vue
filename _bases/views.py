from django.db.models import Q
from django.views.generic import TemplateView, ListView

from celebs.models import Celebrity
from movies.models import Movie


# vue views
class Home(TemplateView):
    template_name = 'vue/home.html'


# html views
class HtmlHome(ListView):
    template_name = 'html/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['celebs'] = Celebrity.objects.prefetch_related(
            'moviecrews__duty', 'moviecrews__crew', 'comments'
        ).order_by('-pk')[:3]
        context['celeb_title'] = 'Celebrities'
        context['movie_title'] = 'Latest Added Movies'
        return context

    def get_queryset(self):
        return Movie.objects \
            .prefetch_related(
                'moviecrews__duty', 'moviecrews__crew',
                'genres', 'comments') \
            .order_by('-pk', 'name')[:3]


class HtmlSearchResultsView(ListView):
    template_name = 'html/search.html'

    def get_context_data(self, **kwargs):
        query = str(self.request.GET.get('q'))
        context = super().get_context_data(**kwargs)
        context['q'] = query
        context['celebs'] = Celebrity.objects \
            .filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)) \
            .values_list(
                'pk', 'slug', 'first_name', 'last_name', named=True)
        context['celeb_title'] = 'Found Celebrities'
        context['movie_title'] = 'Found Movies'
        context['movie_title_small'] = 'ordered by release date'
        return context

    def get_queryset(self):
        query = str(self.request.GET.get('q')).strip()
        return Movie.objects.filter(Q(name__icontains=query)).values_list(
            'pk', 'slug', 'name', named=True
        ).order_by('-release_year', 'name')
