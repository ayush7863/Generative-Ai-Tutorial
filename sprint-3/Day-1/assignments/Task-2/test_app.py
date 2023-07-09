
import pytest

from flask import Response
from app import create_app


weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize('city', weather_data.keys())
def test_weather_endpoint(client, city):
    response = client.get(f'/weather/{city}')
    data = response.get_json()

    if response.status_code == 200:
        assert response.status_code == 200
        assert data == weather_data[city]
    else:
        assert "Test failed"


@pytest.mark.parametrize('city, weather_info', weather_data.items())
def test_create_weather(client, city, weather_info):

    response = client.post('/create', json=weather_info)
    data = response.get_json()
    if response.status_code == 201:
        assert response.status_code == 201
        assert data == weather_data[city]
    else:
        assert "Test Failed"


@pytest.mark.parametrize("city", weather_data.keys())
def test_update_weather(client, city):
    response = client.put(f'/update/{city}')
    data = response.get_json()

    if response.status_code == 200:
        assert response.status_code == 200
        assert weather_data[city] == data
    else:
        assert "Test Failed"


@pytest.mark.parametrize("city", weather_data.keys())
def test_delete_weather(client, city):
    response = client.delete(f'/delete/{city}')
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        assert "Test Failed"
