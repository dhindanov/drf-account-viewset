import pytest
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def get_authenticated_client(monkeypatch):
    def _get_authenticated_client(user: User):
        def authenticate(*args): return user, None

        client = APIClient()
        client.force_authenticate(user=user)
        return client

    return _get_authenticated_client
