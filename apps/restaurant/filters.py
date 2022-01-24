import django_filters
from django.db.models import QuerySet

from apps.restaurant.models import Restaurant


class RestarauntFilter(django_filters.FilterSet):

    randomize = django_filters.BooleanFilter(method='filter_randomize')

    class Meta:
        model = Restaurant
        fields = ['randomize']

    def filter_randomize(self, queryset: QuerySet, name: str, value: bool) -> QuerySet:
        return queryset.order_by('?') if value else queryset
