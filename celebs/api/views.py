from rest_framework import viewsets
from rest_framework.response import Response

from movies.models import MovieCrew
from celebs.models import Duty, Celebrity
from .serializers import (
    DutySerializer, CelebritySerializer, MovieCrewSerializer)


class DutyViewSet(viewsets.ModelViewSet):
    queryset = Duty.objects.prefetch_related('celebs')
    serializer_class = DutySerializer
    lookup_field = 'slug'


class CelebrityViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.prefetch_related('duties')
    serializer_class = CelebritySerializer
    lookup_field = 'slug'


class MovieCrewViewSet(viewsets.ViewSet):
    # permission_classes =

    def list(self, request, slug=None):
        queryset = MovieCrew.objects.select_related(
            'movie', 'crew').filter(crew__slug=slug)
        serializer = MovieCrewSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
