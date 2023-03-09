from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from apps.tracks.filters import AlbumFilter
from apps.tracks.models import Album, Track, Songwriter
from apps.tracks.serializers import AlbumSerializer, TrackSerializer, SongwriterSerializer


class AlbumViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AlbumFilter


class TrackViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class SongwriterViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = SongwriterSerializer
    queryset = Songwriter.objects.all()
