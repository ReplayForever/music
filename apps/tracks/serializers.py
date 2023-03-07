from rest_framework import serializers

from apps.tracks.models import Track, Album, Songwriter


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ['id', 'title', 'year', ]


class AlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'year', 'genre', 'track', ]


class SongwriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songwriter
        fields = ['id', 'name', ]
