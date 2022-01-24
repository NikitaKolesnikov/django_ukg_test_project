from django.db.models import Max
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from apps.restaurant.models import Restaurant
from tests.restaurant_api.base import BaseRestaurantAPITestCase


class RestaurantDetailAPITestCase(BaseRestaurantAPITestCase):
    def test_response(self) -> None:
        response: Response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_content(self) -> None:
        response: Response = self.client.get(self.detail_url)

        self.assertEqual(response.data['id'], self.default_restaurant.id)
        self.assertEqual(response.data['name'], self.default_restaurant.name)
        self.assertEqual(
            response.data['description'], self.default_restaurant.description
        )

    def test_wrong_id(self) -> None:
        max_id: int = Restaurant.objects.filter().aggregate(max_id=Max('id'))['max_id']
        url: str = reverse(
            'restaurant-api:retrieve-update-destroy', kwargs={'pk': max_id + 1}
        )
        response: Response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
