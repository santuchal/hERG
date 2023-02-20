import pytest

from src.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(client):
    assert client.get("/").status_code == 200