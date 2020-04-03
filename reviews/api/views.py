from rest_framework import viewsets

from reviews.models import CelebComment, MovieComment
from .serializers import CelebCommentSerializer, MovieCommentSerializer


class CelebCommentViewSet(viewsets.ModelViewSet):
    queryset = CelebComment.objects.select_related('celeb')
    serializer_class = CelebCommentSerializer


class MovieCommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.select_related('movie')
    serializer_class = MovieCommentSerializer
