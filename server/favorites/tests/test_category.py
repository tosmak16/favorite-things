from django.urls import reverse
from rest_framework import status

from .test_base import TestBase


class CategoryTests(TestBase):

    url = reverse('categories-list')

    def test_get_category_success(self):
        """
        Gets categories successfully
        """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], self.category_data['name'])

    def test_create_category_success(self):
        """
        Create Category success
        """

        category_data = self.category_data.copy()
        category_data['name'] = 'movie'

        response = self.client.post(self.url, category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], category_data['name'])

    def test_create_category_fail(self):
        """
        Create Category fail empty name
        """

        category_data = self.category_data.copy()
        category_data['name'] = ''

        response = self.client.post(self.url, category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0],
                         'This field may not be blank.')

    def test_get_favorite_in_category_success(self):
        """
        Get Category's favorites success
        """

        self.favorite_1.category.__str__()

        self.url = reverse('category_favorite', kwargs={
                           'category_id': self.category_1.id})

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'],
                         self.favorite_data['title'])
