from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import CreditCard


class CreditCardAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="cardtestuser",
            password="TestPassword123"
        )

        self.client.force_authenticate(
            user=self.user
        )

        self.card_data = {
            "card_holder_name": "Test User",
            "masked_card_number": "**** **** **** 1234",
            "last_four_digits": "1234"
        }

    def test_create_card(self):
        response = self.client.post(
            "/api/credit-cards/",
            self.card_data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_cards(self):
        CreditCard.objects.create(**self.card_data)

        response = self.client.get(
            "/api/credit-cards/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_card(self):
        card = CreditCard.objects.create(
            **self.card_data
        )

        response = self.client.delete(
            f"/api/credit-cards/{card.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_cards_require_authentication(self):
        self.client.force_authenticate(user=None)

        response = self.client.get(
            "/api/credit-cards/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )