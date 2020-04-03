from django.urls import path

from .views import (
    HtmlCelebrityList, HtmlCelebrityDetail)

urlpatterns = [
    # html urls
    path('<slug:slug>/',
         HtmlCelebrityDetail.as_view(), name='html_celeb_detail'),
    path('', HtmlCelebrityList.as_view(), name='html_celeb_list')
]
