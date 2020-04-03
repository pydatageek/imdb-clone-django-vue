from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CelebCommentViewSet, MovieCommentViewSet

router = DefaultRouter()
router.register('celebcomment', CelebCommentViewSet)
router.register('moviecomment', MovieCommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
