import django_filters
from django.db.models import Q


class ListFilter(django_filters.Filter):
    def sanitize(self, value_list):
        """
        Remove empty values
        """
        return [value for value in value_list if value != u'']

    def filter(self, qs, value):
        """
        Filter for multiple values for endpoints
        """
        try:
            value_list = value.split(u',')
            value_list = self.sanitize(value_list)
        except AttributeError:
            """Raise when value_list is empty"""
            return qs
        filter_param = Q()
        for value in value_list:
            kwargs = {self.field_name: value}
            filter_param = filter_param | Q(**kwargs)
        return qs.filter(filter_param)


