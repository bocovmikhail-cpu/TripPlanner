from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.test import TestCase
from rest_framework.test import APIClient

User = get_user_model()


class RegisterUserTests(TestCase):
    def test_register_creates_user(self):
        client = APIClient()

        response = client.post(
            "/api/auth/register/",
            {"username": "alice", "password": "secret123"},
            format="json",
        )

        assert isinstance(response, HttpResponse)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username="alice").exists())
