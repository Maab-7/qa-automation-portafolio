import pytest
from utils.api_client import get, post

@pytest.fixture(scope="session")
def existing_user_id():
    """Returns a valid user ID fetched from the API."""
    response = get("/users", params={"page": 1})
    users = response.json()["data"]
    return users[0]["id"]

@pytest.fixture(scope="session")
def created_user():
    """Creates a user via POST and returns the response data."""
    payload = {
        "name": "Marco Alfaro",
        "job": "QA Engineer"
    }
    response = post("/users", payload)
    return response.json()

@pytest.fixture(scope="session")
def auth_token():
    """Logs in and returns a valid auth token"""
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = post("/login", payload)
    return response.json()["token"]
