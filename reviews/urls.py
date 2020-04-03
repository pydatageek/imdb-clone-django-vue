from django.urls import path

from .views import (
    MovieCommentList, MovieCommentDetail,
    CelebCommentList, CelebCommentDetail)

urlpatterns = [
    path('movie/', MovieCommentList.as_view(
        template_name='reviews/moviecomment_list.html'),
        name='moviecomment_list'),
    path('movie/<slug:slug>/', MovieCommentDetail.as_view(
        template_name='reviews/moviecomment_detail.html'),
        name='moviecomment_detail'),
    path('celeb/', CelebCommentList.as_view(
        template_name='reviews/celebcomment_list.html'),
        name='celebcomment_list'),
    path('celeb/<slug:slug>/', CelebCommentDetail.as_view(
        template_name='reviews/celebcomment_detail.html'),
        name='celebcomment_detail'),
]
