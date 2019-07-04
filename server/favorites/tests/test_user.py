from django.urls import reverse
from rest_framework import status
from django.urls import reverse

from .test_base import TestBase


class UserRegisterTests(TestBase):

    url = reverse('users')

    user_test_data = {
        'email': 'test2@test.com',
        'password': 'testpassword2',
        'username': 'test_username2'
    }

    def test_register_user_successful(self):
        """
        User registers successfully
        """

        user_data = self.user_test_data.copy()

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Login successful.')

    def test_register_user_failed_no_email(self):
        """
        Register user failed due to no email
        """

        user_data = self.user_test_data.copy()
        user_data.pop('email')

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'This field is required.')

    def test_register_user_failed_invalid_email(self):
        """
        Register user failed due to invalid email
        """

        user_data = self.user_test_data.copy()
        user_data['email'] = "aaa"

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0],
                         'Enter a valid email address.')

    def test_register_user_failed_no_username(self):
        """
        Register user failed due to no username
        """

        user_data = self.user_test_data.copy()
        user_data.pop('username')

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0],
                         'This field is required.')

    def test_register_user_failed_no_password(self):
        """
        Register user failed due to no password
        """

        user_data = self.user_test_data.copy()
        user_data.pop('password')

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0],
                         'This field is required.')

    def test_register_user_failed_user_already_exist(self):
        """
        Register users failed due to user already_exist
        """

        user_data = self.user_data.copy()

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0],
                         'A user with that username already exists.')


class UserLoginTests(TestBase):

    url = reverse('login')

    def test_login_user_successful(self):
        """
        User Login successfully
        """

        user_data = self.user_data.copy()

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Login successful.')

    def test_login_user_failed_invalid_data(self):
        """
        User login failed due to invalid credentials
        """

        user_data = self.user_data.copy()
        user_data['username'] = 'test'

        response = self.client.post(self.url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Wrong Credentials.')
