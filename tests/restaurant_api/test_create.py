from typing import Dict

from rest_framework import status
from rest_framework.response import Response

from apps.restaurant.models import Restaurant
from tests.factories import RestaurantFactory
from tests.restaurant_api.base import BaseRestaurantAPITestCase


class RestaurantCreateAPITestCase(BaseRestaurantAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.default_data: Dict = {
            'name': 'Test create: name',
            'description': 'Test create: description',
        }

    def test_successful_response(self) -> None:
        response: Response = self.client.post(self.list_url, data=self.default_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_successful_response_content(self) -> None:
        response: Response = self.client.post(self.list_url, data=self.default_data)
        keys: list = response.data.keys()

        self.assertIn('id', keys)
        self.assertIn('name', keys)
        self.assertIn('description', keys)

    def test_created_object(self) -> None:
        response: Response = self.client.post(self.list_url, data=self.default_data)
        restaurant = Restaurant.objects.get(id=response.data['id'])

        self.assertEqual(self.default_data['name'], restaurant.name)
        self.assertEqual(self.default_data['description'], restaurant.description)

    def test_required_fields(self) -> None:
        response: Response = self.client.post(self.list_url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data.keys())
        self.assertIn('description', response.data.keys())

    def test_unique_name(self) -> None:
        existing_restaurant = RestaurantFactory(name='Existing restaurant 1')
        response: Response = self.client.post(
            self.list_url,
            data={
                'name': existing_restaurant.name,
                'description': 'Test create with unique name: description',
            },
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data.keys())
