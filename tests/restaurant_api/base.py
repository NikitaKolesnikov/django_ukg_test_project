from django.urls import reverse
from rest_framework.test import APITestCase

from tests.factories import RestaurantFactory


class BaseRestaurantAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.default_restaurant = RestaurantFactory()
        self.list_url = reverse('restaurant-api:list-create')
        self.detail_url = reverse(
            'restaurant-api:retrieve-update-destroy',
            kwargs={'slug': self.default_restaurant.slug},
        )
