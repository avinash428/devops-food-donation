from django.test import TestCase
from django.urls import reverse

class LoginURLTest(TestCase):
    def test_login_url_exists(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

class SignupURLTest(TestCase):
    def test_login_url_exists(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

class IndexURLTest(TestCase):
    def test_login_url_exists(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

