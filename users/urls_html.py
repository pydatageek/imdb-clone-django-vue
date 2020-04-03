from django.urls import path

from .views import (
    GroupList)

urlpatterns = [
    # html urls
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('profile/movies/', views.UserMovieView.as_view(), name='user_movies'),
    # path('profile/movies2/', views.UserMovieViewWithLoop.as_view(),
    #      name='user_movies2'),
]
