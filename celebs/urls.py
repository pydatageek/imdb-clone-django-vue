from django.urls import path

from .views import (
    DutyList, DutyDetail, CelebrityList, CelebrityDetail)

urlpatterns = [
    # vue urls
    path('duty/<slug:slug>/', DutyDetail.as_view(), name='duty_detail'),
    path('duty/', DutyList.as_view(), name='duty_list'),
    path('<slug:slug>/', CelebrityDetail.as_view(), name='celeb_detail'),
    path('', CelebrityList.as_view(), name='celeb_list'),
]
