from rest_framework import serializers

from apps.tracks.models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title', 'year', ]


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer()

    class Meta:
        model = Track
        fields = ['id', 'title', 'year', 'genre', 'tracks', ]

