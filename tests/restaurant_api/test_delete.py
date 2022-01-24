from rest_framework import status
from rest_framework.response import Response

from apps.restaurant.models import Restaurant
from tests.restaurant_api.base import BaseRestaurantAPITestCase


class RestaurantDeleteAPITestCase(BaseRestaurantAPITestCase):
    def test_response(self) -> None:
        response: Response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_object_deleted(self) -> None:
        self.client.delete(self.detail_url)

        self.assertEqual(
            Restaurant.objects.filter(id=self.default_restaurant.id).count(), 0
        )
