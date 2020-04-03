from django.views.generic import TemplateView


# vue views
class UserList(TemplateView):
    template_name = 'vue/users/user_list.html'


class UserDetail(TemplateView):
    template_name = 'vue/users/user_detail.html'


class FavoriteGenreList(TemplateView):
    template_name = 'vue/users/user_genre_list.html'


class FavoriteGenreDetail(TemplateView):
    template_name = 'vue/users/user_genre_detail.html'


class FavoriteMovieList(TemplateView):
    template_name = 'vue/users/user_movie_list.html'


class FavoriteMovieDetail(TemplateView):
    template_name = 'vue/users/user_movie_detail.html'


class FavoriteCelebList(TemplateView):
    template_name = 'vue/users/user_celeb_list.html'


class FavoriteCelebDetail(TemplateView):
    template_name = 'vue/users/user_celeb_detail.html'


class GroupList(TemplateView):
    template_name = 'vue/users/group_list.html'


class GroupDetail(TemplateView):
    template_name = 'vue/users/group_detail.html'


# html views
"""
class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_success_message(self, cleaned_data):
        return f'Welcome {cleaned_data["username"]}! Thank you for joining us.'


class ProfileBaseView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    pass


class ProfileView(ProfileBaseView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'Your profile has been updated'

    def get_object(self):
        user = self.request.user
        return User.objects.get(username=user.username)


class UserMovieView(LoginRequiredMixin, CreateView):
    # TODO
    # It doesn't work now!
    # This is the View that should be one page!

    model = UserMovie
    template_name = 'users/user-movies.html'
    success_url = reverse_lazy('users:user_movies')
    fields = ('user', 'movie', 'note', 'watched', 'watch_list')

    def get_context_data(self, **kwargs):
        context = super(UserMovieView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['usermovies'] = UserMovieFormSet(self.request.POST)
        else:
            context['usermovies'] = UserMovieFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        usermovies = context['usermovies']
        with transaction.atomic():
            self.object = form.save()
            if usermovies.is_valid():
                usermovies.instance = self.object
                usermovies.save()
        return super(UserMovieView, self).form_valid(form)

    # def get_object(self):
    #     user = self.request.user
    #     return UserMovie.objects.get(user=user)


class UserMovieViewWithLoop(LoginRequiredMixin, CreateView):
    model = UserMovie
    template_name = 'users/user-movies-with_loop.html'
    form_class = UserMovieFormWithLoop
    success_message = 'your form has been submitted.'
    success_url = reverse_lazy('users:user_movies2')

    def form_valid(self, form):
        user = self.request.user
        movie_counter = Movie.objects.filter(
            genres__in=user.genres.all()).count()
        f = form.save(commit=False)
        f.user = user
        for i in range(movie_counter):
            f.pk = None
            f.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserMovieViewWithLoop, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def get_object(self):
        user = self.request.user
        return UserMovie.objects.get(user=user)
"""
