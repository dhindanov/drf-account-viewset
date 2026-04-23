import pytest


@pytest.mark.django_db
def test_api_root(client):
    response = client.get('/api/')
    assert response.status_code == 200
