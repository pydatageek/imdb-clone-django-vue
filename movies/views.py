from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .forms import CommentForm
from .models import Genre, Movie


# vue views
class GenreList(TemplateView):
    template_name = 'vue/movies/genre_list.html'


class GenreDetail(TemplateView):
    template_name = 'vue/movies/genre_detail.html'


class PgRatingList(TemplateView):
    template_name = 'vue/movies/pg_rating_list.html'


class PgRatingDetail(TemplateView):
    template_name = 'vue/movies/pg_rating_detail.html'


class MovieList(TemplateView):
    template_name = 'vue/movies/movie_list.html'


class MovieDetail(TemplateView):
    template_name = 'vue/movies/movie_detail.html'


# html views
pagination = 5


class MovieListMixin(ListView):
    """It returns movies with prefetched related"""
    template_name = 'html/movies/movie_list.html'
    queryset = Movie.objects.prefetch_related(
        'moviecrews__duty', 'moviecrews__crew', 'genres', 'comments')
    paginate_by = pagination


class HtmlMovieList(MovieListMixin):
    """All movies ordered by release date desc"""
    ordering = ('-release_year', 'name')  # is it needed?

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Latest movies')
        context['title_suffix'] = _('by release date')
        return context


class HtmlTopMovieList(MovieListMixin):
    """All movies ordered by imdb rating desc"""
    ordering = ('-imdb_rating', 'name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Top movies'
        context['title_suffix'] = 'on IMDB'
        return context


class HtmlMovieDetail(SuccessMessageMixin, DetailView, CreateView):
    template_name = 'html/movies/movie_detail.html'
    queryset = Movie.objects.prefetch_related(
        'moviecrews__duty', 'moviecrews__crew',
        'genres', 'comments__added_by')  # or only comments
    form_class = CommentForm
    success_message = _('Your comment has been sent succesfully!')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse(
            'html_movie_detail',
            kwargs={
                'slug': self.object.movie.slug
            }
        )


class HtmlGenreList(ListView):
    template_name = 'html/movies/genre_list.html'
    queryset = Genre.objects.prefetch_related('movies')


class HtmlGenreMovieList(ListView):
    template_name = 'html/movies/movie_list.html'
    paginate_by = pagination

    def get_queryset(self):
        return Movie.objects \
            .filter(genres__slug__icontains=self.kwargs['slug']) \
            .order_by('-release_year', 'name') \
            .prefetch_related(
                'moviecrews__duty', 'moviecrews__crew',
                'genres', 'comments')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        genre = str(self.kwargs['slug']).title()
        context['title'] = f'Latest {genre} movies'
        context['title_suffix'] = 'by release date'
        return context
