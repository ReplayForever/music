from rest_framework import serializers

from apps.commons.choices import Genres
from apps.tracks.models import Track, Album, Songwriter


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ['id', 'title', 'year', 'songwriter']


class AlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer(many=True, read_only=True)
    songwriter = serializers.CharField(source='songwriter.name')
    genre = serializers.CharField(source='get_genre_display')

    class Meta:
        model = Album
        fields = ['id', 'title', 'year', 'genre', 'songwriter', 'track', ]


class SongwriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songwriter
        fields = ['id', 'name', ]
