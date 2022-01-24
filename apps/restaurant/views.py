from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.restaurant import serializers, filters
from apps.restaurant.models import Restaurant


class RestaurantListCreateView(generics.ListCreateAPIView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_class = filters.RestarauntFilter
    search_fields = ['name']


class RestaurantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    lookup_field = 'slug'
