from django.test import TestCase
from django.urls import reverse

class LoginURLTest(TestCase):
    def test_login_url_exists(self):
        """Test if the login URL exists and returns a 200 status code"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)