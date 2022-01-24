from rest_framework import status
from rest_framework.response import Response

from apps.restaurant.models import Restaurant
from tests.factories import RestaurantFactory
from tests.restaurant_api.base import BaseRestaurantAPITestCase


class RestaurantListAPITestCase(BaseRestaurantAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        RestaurantFactory.create_batch(15)

    def test_response(self) -> None:
        response: Response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_content(self) -> None:
        response: Response = self.client.get(self.list_url)
        keys: list = response.data[0].keys()

        self.assertEqual(len(response.data), Restaurant.objects.count())
        self.assertIn('id', keys)
        self.assertIn('name', keys)
        self.assertIn('description', keys)
