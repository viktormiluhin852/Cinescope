import pytest
import requests
from constants import BASE_URL, HEADERS
from faker import Faker

faker = Faker("ru_RU")

@pytest.fixture
def auth_session():

    s = requests.Session()
    s.headers.update(HEADERS)

    response = s.post(f"{BASE_URL}/auth", json={"username": "admin",
    "password": "password123"})

    assert response.status_code == 200

    token = response.json().get("token")

    s.headers.update({"Cookie": f"token={token}"})

    return s

@pytest.fixture
def auth_session1():

    s = requests.Session()
    s.headers.update(HEADERS)

    response = s.post(f"{BASE_URL}/auth", json={"username": "admin1",
    "password": "password123"})

    assert response.status_code == 200

    token = response.json().get("token")

    s.headers.update({"Cookie": f"token={token}"})

    return s

@pytest.fixture
def post_data():
    return {
    "firstname" : faker.first_name(),
    "lastname" : faker.last_name(),
    "totalprice" : faker.random_int(min=100, max=100000),
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

@pytest.fixture
def put_data():
    return {
    "firstname" : faker.first_name(),
    "lastname" : faker.last_name(),
    "totalprice" : faker.random_int(min=100, max=100000),
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}




