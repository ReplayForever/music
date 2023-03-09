from django_filters import rest_framework as filters

from apps.commons.filters import ListFilter
from apps.tracks.models import Album


class AlbumFilter(filters.FilterSet):
    year = ListFilter(field_name='year')
    songwriter = ListFilter(field_name='songwriter__name__icontains')
    title = ListFilter(field_name='title__icontains')

    class Meta:
        model = Album
        fields = [
            'songwriter',
            'title',
            'year',
        ]
