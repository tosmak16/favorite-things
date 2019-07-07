from django.urls import reverse
from rest_framework import status

from .test_base import TestBase


class AuditLogsTests(TestBase):

    url = reverse('audit_logs')

    def test_get_favorite_success(self):
        """
        Get audit logs success
        """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
