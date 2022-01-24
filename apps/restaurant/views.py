from django.shortcuts import render
from rest_framework import generics

from apps.restaurant.models import Restaurant
from apps.restaurant import serializers


class RestaurantListCreateView(generics.ListCreateAPIView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class RestaurantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
