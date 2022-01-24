from django.urls import path

from apps.restaurant import views


restaurant_api_urls = (
    [
        path(
            '',
            views.RestaurantListCreateView.as_view(),
            name='list-create',
        ),
        path(
            '<str:slug>',
            views.RestaurantRetrieveUpdateDestroyView.as_view(),
            name='retrieve-update-destroy',
        ),
    ],
    'restaurant-api',
)
