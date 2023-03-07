from rest_framework import viewsets, mixins

from apps.tracks.models import Album, Track
from apps.tracks.serializers import AlbumSerializer, TrackSerializer


class AlbumViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class TrackViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()

