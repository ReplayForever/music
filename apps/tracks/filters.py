from django_filters import rest_framework as filters

from apps.commons.filters import ListFilter
from apps.tracks.models import Album


class AlbumFilter(filters.FilterSet):
    # year = filters.CharFilter(method='filter_by_year', field_name='year')
    songwriter = ListFilter(field_name='songwriter__name')
    title = filters.CharFilter(field_name='title')

    class Meta:
        model = Album
        fields = [
            'songwriter',
            'title',
        ]
