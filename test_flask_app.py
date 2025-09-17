import pytest
from flask_app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Jenkins CI/CD!" in response.data

def test_add(client):
    """Test the add route"""
    response = client.get('/add/2/3')
    assert response.status_code == 200
    assert response.data == b"5"