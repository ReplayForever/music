from rest_framework import viewsets

from apps.tracks.models import Album
from apps.tracks.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

