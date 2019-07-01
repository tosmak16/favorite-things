from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from ..models import Category, Favorite


class TestBase(APITestCase):

    def setUp(self):

        self.user_data = {
            'email': 'test@test.com',
            'password': 'testpassword',
            'username': 'test_username'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

        self.token = Token.objects.create(user=self.user)
        self.token.save()

        # call setup category function
        self.setup_category()

        # call setup favorite function
        self.setup_favorite()

        # authenticate user
        self.login_setup()

    def setup_category(self):

        self.category_data = dict(name='sport')

        self.category_data_2 = dict(name='game')

        self.category_1 = Category(**self.category_data)
        self.category_2 = Category(**self.category_data_2)

        self.category_1.save()
        self.category_2.save()

    def login_setup(self):
        user_data = self.user_data.copy()
        self.client.login(**user_data)

    def setup_favorite(self):

        self.favorite_data = dict(
            title="Fifa 19",
            description="Best football game",
            owner=self.user,
            metadata="",
            category=self.category_1,
            ranking=3
        )

        self.favorite_1 = Favorite(**self.favorite_data)
        self.favorite_1.save()
