from django.urls import reverse
from rest_framework import status
from django.urls import reverse

from .test_base import TestBase


class FavoriteTests(TestBase):

    url = reverse('favorites-list')

    def test_get_favorite_success(self):
        """
        Get favorites success
        """

        self.favorite_1.__str__()

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'],
                         self.favorite_data['title'])
        self.assertEqual(response.data[0]['ranking'],
                         self.favorite_data['ranking'])

    def test_create_favorite_success(self):
        """
        Create favorite success
        """

        favorite_data = self.favorite_data.copy()
        favorite_data['title'] = 'Wrestling'
        favorite_data['owner'] = self.user.id
        favorite_data['category'] = self.category_1.id
        favorite_data['ranking'] = 1

        response = self.client.post(self.url, favorite_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], favorite_data['title'])


class FavoriteDetailTests(TestBase):

    def test_get_single_favorite_success(self):
        """
        Get a single favorite success
        """

        url = reverse('favorites-detail', kwargs={'pk': self.favorite_1.id})

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'],
                         self.favorite_data['title'])
        self.assertEqual(response.data['ranking'],
                         self.favorite_data['ranking'])

    def test_update_favorite_ranking_with_same_value_success(self):
        """
        It updates favorite ranking with same value
        """

        url = reverse('favorites-detail', kwargs={'pk': self.favorite_1.id})

        favorite_data = self.favorite_data.copy()
        favorite_data['owner'] = self.user.id
        favorite_data['category'] = self.category_1.id

        response = self.client.put(url, favorite_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ranking'], favorite_data['ranking'])

    def test_update_favorite_ranking_with_higher_value_success(self):
        """
        It updates favorite ranking with higher value
        """

        url = reverse('favorites-detail', kwargs={'pk': self.favorite_1.id})

        favorite_data = self.favorite_data.copy()
        favorite_data['owner'] = self.user.id
        favorite_data['category'] = self.category_1.id
        favorite_data['ranking'] = 4

        response = self.client.put(url, favorite_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(response.data['ranking'],
                           self.favorite_data['ranking'])

    def test_update_favorite_ranking_with_lower_value_success(self):
        """
        It updates favorite ranking with lower value
        """

        url = reverse('favorites-detail', kwargs={'pk': self.favorite_1.id})

        favorite_data = self.favorite_data.copy()
        favorite_data['title'] = 'Wrestling'
        favorite_data['owner'] = self.user.id
        favorite_data['category'] = self.category_1.id
        favorite_data['ranking'] = 2

        response = self.client.put(url, favorite_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(response.data['ranking'],
                        self.favorite_data['ranking'])

    def test_update_favorite_category_with_different_value_success(self):
        """
        It updates favorite category with different value
        """

        url = reverse('favorites-detail', kwargs={'pk': self.favorite_1.id})

        favorite_data = self.favorite_data.copy()
        favorite_data['title'] = 'Wrestling'
        favorite_data['owner'] = self.user.id
        favorite_data['category'] = self.category_2.id
        favorite_data['ranking'] = 1

        response = self.client.put(url, favorite_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], favorite_data['category'])

    def test_delete_single_favorite_success(self):
        """
        Get a single favorite success
        """

        url = reverse('favorites-detail', kwargs={'pk': self.favorite_1.id})

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
