import pytest
from utils.api_client import get, post, put, delete

class TestGetUsers:
    def test_get_users_returns_200(self):
        """GET /users should return HTTP 200"""
        response = get("/users", params={"page":1})
        assert response.status_code == 200

    def test_get_users_returns_list(self):
        """Response body should contain a list of users"""
        response = get("/users", params={"page":1})
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0

    def test_get_single_user_returns_200(self):
        """GET /users/{id} should return HTTP 200 for existing user"""
        response = get("/users/2")
        assert response.status_code == 200

    def test_get_single_user_returns_id(self):
        """Response body should contain the correct user ID"""
        response = get("/users/2")
        data = response.json()
        assert data["data"]["id"] == 2

    def test_get_nonexistent_user_returns_404(self):
        """GET /users/{id} should return HTTP 404 for non-existent user"""
        response = get("/users/9999")
        assert response.status_code == 404
    
    