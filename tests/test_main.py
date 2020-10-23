from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'msg': 'Welcome to Simple Geocoding Service'}


def test_geocode_service():
    address_json = {
      "address": "Meru",
      "town": "Klang",
      "postcode": "41050",
      "country": "my"
    }

    response = client.post("/geocode", json=address_json)
    assert response.status_code == 200
    assert response.json() == {
                                  "address": "Meru",
                                  "town": "Klang",
                                  "postcode": "41050",
                                  "country": "my",
                                  "latitude": 3.0645,
                                  "longitude": 101.4786
                                }


def test_delete_address():

    address_json = {
      "address": "Meru",
      "town": "Klang",
      "postcode": "41050",
      "country": "my"
    }

    response = client.post("/geocode", json=address_json)
    assert response.status_code == 200

    response2 = client.delete('/addresses/0')
    assert response2.status_code == 200
    assert response2.json() == {}


def test_get_address():
    address_json = {
        "address": "Meru",
        "town": "Klang",
        "postcode": "41050",
        "country": "my"
    }

    response = client.post("/geocode", json=address_json)
    assert response.status_code == 200
    assert response.json() == {
        "address": "Meru",
        "town": "Klang",
        "postcode": "41050",
        "country": "my",
        "latitude": 3.0645,
        "longitude": 101.4786
    }

    response2 = client.get('/addresses/0')
    assert response2.status_code == 200
    assert response.json() == {
        "address": "Meru",
        "town": "Klang",
        "postcode": "41050",
        "country": "my",
        "latitude": 3.0645,
        "longitude": 101.4786
    }

