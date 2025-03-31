from django.test import TestCase, Client
from django.urls import reverse

class LoginTestCase(TestCase):
    def setUp(self):
        """Set up the client for sending requests."""
        self.client = Client()

    #Admin login test
    def test_admin_login(self):
        response = self.client.post(reverse("login"), {
            "email": "admin@gmail.com",
            "password": "admin"
        })
        self.assertRedirects(response, reverse("admin_dashboard"))
        self.assertEqual(self.client.session.get("user_id"), 1)



    #Invalid credentials test
    def test_invalid_login(self):
        response = self.client.post(reverse("login"), {
            "email": "invalid@example.com",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
