from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User


class UserAuthenticationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123"
        )

    def test_user_created(self):
        self.assertTrue(
            User.objects.filter(username="testuser").exists()
        )

    def test_password_is_hashed(self):
        self.assertNotEqual(
            self.user.password,
            "TestPassword123"
        )

    def test_correct_password(self):
        self.assertTrue(
            self.user.check_password("TestPassword123")
        )

    def test_wrong_password(self):
        self.assertFalse(
            self.user.check_password("WrongPassword")
        )