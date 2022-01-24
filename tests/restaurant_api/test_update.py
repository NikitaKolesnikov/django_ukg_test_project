from typing import Dict

from rest_framework import status
from rest_framework.response import Response

from tests.restaurant_api.base import BaseRestaurantAPITestCase


class RestaurantUpdateAPITestCase(BaseRestaurantAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.default_data: Dict = {
            'name': 'Test update: name',
            'description': 'Test update: description',
        }

    def test_successful_response(self) -> None:
        response: Response = self.client.put(self.detail_url, data=self.default_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_successful_response_content(self) -> None:
        response: Response = self.client.put(self.detail_url, data=self.default_data)
        keys: list = response.data.keys()

        self.assertIn('id', keys)
        self.assertIn('name', keys)
        self.assertIn('description', keys)

    def test_updated_object(self) -> None:
        self.client.put(self.detail_url, data=self.default_data)
        self.default_restaurant.refresh_from_db()

        self.assertEqual(self.default_data['name'], self.default_restaurant.name)
        self.assertEqual(
            self.default_data['description'], self.default_restaurant.description
        )

    def test_required_fields(self) -> None:
        response: Response = self.client.put(self.detail_url, data={})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data.keys())
        self.assertIn('description', response.data.keys())


class RestaurantPartialUpdateAPITestCase(BaseRestaurantAPITestCase):
    def test_successful_response(self) -> None:
        response: Response = self.client.patch(
            self.detail_url, data={'name': 'Test partial update: name'}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_updated_object(self) -> None:
        old_name = self.default_restaurant.name
        data: Dict = {'description': 'Test partial update: description'}
        self.client.patch(self.detail_url, data=data)
        self.default_restaurant.refresh_from_db()

        self.assertEqual(old_name, self.default_restaurant.name)
        self.assertEqual(data['description'], self.default_restaurant.description)
