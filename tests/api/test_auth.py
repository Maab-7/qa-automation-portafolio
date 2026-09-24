import pytest
from utils.api_client import post

class TestLogin:
    @pytest.mark.smoke
    def test_login_returns_200(self):
        """POST /login with valid credentials should return HTTP 200"""
        payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = post("/login", payload)
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_login_returns_token(self):
        """POST /login should return a token in the response body"""
        payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = post("/login", payload)
        data = response.json()
        assert "token" in data
        assert data["token"] is not None

    @pytest.mark.regression
    def test_login_missing_password_returns_400(self):
        """POST /login without password should return HTTP 400"""
        payload = {"email": "eve.holt@reqres.in"}
        response = post("/login", payload)
        assert response.status_code == 400

    @pytest.mark.regression
    def test_login_missing_password_returns_error_message(self):
        """POST /login without password should return an error message"""
        payload = {"email": "eve.holt@reqres.in"}
        response = post("/login", payload)
        data = response.json()
        assert "error" in data

    @pytest.mark.regression
    def test_login_invalid_credentials_returns_400(self):
        """POST /login with unknown email should return HTTP 400"""
        payload = {"email": "unknown@reqres.in", "password": "wrongpass"}
        response = post("/login", payload)
        assert response.status_code == 400


class TestRegister:

    @pytest.mark.smoke
    def test_register_returns_200(self):
        """POST /register with valid credentials should return HTTP 200"""
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = post("/register", payload)
        assert response.status_code == 200

    @pytest.mark.regression
    def test_register_returns_token(self):
        """POST /register should return a token"""
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = post("/register", payload)
        data = response.json()
        assert "token" in data

    @pytest.mark.regression
    def test_register_missing_password_returns_400(self):
        """POST /register without password should return HTTP 400"""
        payload = {"email": "eve.holt@reqres.in"}
        response = post("/register", payload)
        assert response.status_code == 400

    @pytest.mark.regression
    def test_register_missing_password_returns_error(self):
        """POST /register without password should return error message"""
        payload = {"email": "eve.holt@reqres.in"}
        response = post("/register", payload)
        data = response.json()
        assert "error" in data