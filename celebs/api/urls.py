from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import DutyViewSet, CelebrityViewSet, MovieCrewViewSet

router = DefaultRouter()
router.register('duty', DutyViewSet)
router.register('celeb', CelebrityViewSet)

movie_crews = MovieCrewViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('celeb/<slug:slug>/movies/', movie_crews),
    path('', include(router.urls))
]
