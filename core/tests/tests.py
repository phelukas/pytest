from rest_framework.test import APIClient
import pytest

client = APIClient()


@pytest.mark.django_db
def test_get_song(songs):
    response = client.get('/songs')
    assert response.status_code == 200
