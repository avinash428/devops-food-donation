""" from django.test import TestCase
from django.urls import reverse

class LoginURLTest(TestCase):
    def test_login_url_exists(self):
        #Test if the login URL exists and returns a 200 status code
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200) """

from django.test import TestCase, Client
import MySQLdb
import os

class HouseholdAddDonationTest(TestCase):
    def setUp(self):
        """Setup a test client and database connection."""
        self.client = Client()
        self.db = MySQLdb.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            passwd=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "food_donation_x23389770"),
        )
        self.cursor = self.db.cursor()

        # Insert a test household user
        self.cursor.execute("INSERT INTO household (id, name, email) VALUES (1, 'Test User', 'test@example.com')")
        self.db.commit()

    def test_add_donation(self):
        """Test POST request to add a donation."""
        session = self.client.session
        session["user_id"] = 1
        session["location_id"] = 101  # Example location
        session.save()

        response = self.client.post("/household_add_donation/", {
            "food_type": "Rice",
            "quantity": "5",
            "expiry": "2025-04-10",
        })

        # Verify donation is inserted in the database
        self.cursor.execute("SELECT * FROM donation WHERE household_id = 1")
        donation = self.cursor.fetchone()
        self.assertIsNotNone(donation)

        # Verify redirect
        self.assertEqual(response.status_code, 302)  # Redirect after success

    def tearDown(self):
        """Cleanup database after test."""
        self.cursor.execute("DELETE FROM donation WHERE household_id = 1")
        self.cursor.execute("DELETE FROM household WHERE id = 1")
        self.db.commit()
        self.cursor.close()
        self.db.close()
