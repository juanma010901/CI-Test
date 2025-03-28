from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_info(client):
    response = client.get('/info')
    assert response.status_code == 200
    assert b'ola, Docker pipeline funcionando, se hace CI automatico' == response.data
