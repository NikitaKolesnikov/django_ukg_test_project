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

    def test_search_filter(self) -> None:
        desired_restaurant = RestaurantFactory(name='ABCD restaurant')
        RestaurantFactory(name='another restaurant with weird name')
        response: Response = self.client.get(self.list_url, {'search': 'ABCD'})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], desired_restaurant.id)

    def test_random_filter(self) -> None:
        response_1: Response = self.client.get(self.list_url, {'randomize': True})
        response_2: Response = self.client.get(self.list_url, {'randomize': True})

        self.assertEqual(len(response_2.data), len(response_1.data))
        self.assertNotEqual(
            [x['id'] for x in response_1.data], [x['id'] for x in response_2.data]
        )
