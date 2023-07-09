import pytest
from app import create_app

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

# @pytest.fixture
# def app():
#     return create_app()

@pytest.fixture
def client():
    # return app.test_client()
    app = create_app()
    # app.config['weather_data'] = weather_data

    with app.test_client() as client:
        yield client



@pytest.mark.parametrize('city', weather_data.keys())
def test_weather_endpoint(client, city):
    response = client.get(f'/weather/{city}')
    data = response.get_json() 
    

    if response.status_code==200:
        assert response.status_code == 200
        # assert print(f"Response data for {city}: {data}")
        assert data == weather_data[city]
    else:
        assert "Test failed"


   
   
# def test_weather(client):
#     response = client.get('/weather/New York')
#     if response:
#         assert response.status_code == 200
#         assert response.get_json() == {'temperature': 20, 'weather': 'Sunny'}
#     else:
#         # response = app.client().get('/weather/Nonexistent City')
#         assert response.status_code == 404
#         assert response.get_json() == {'error': 'City not found'}

#     return "Test Passed"
