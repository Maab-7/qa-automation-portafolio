import pytest
from utils.api_client import post, put, delete


class TestCreateUser:

    def test_create_user_returns_201(self):
        """POST /users should return HTTP 201"""
        payload = {"name": "Marco Alfaro", "job": "QA Engineer"}
        response = post("/users", payload)
        assert response.status_code == 201

    def test_create_user_returns_name(self):
        """Created user response should contain the submitted name"""
        payload = {"name": "Marco Alfaro", "job": "QA Engineer"}
        response = post("/users", payload)
        data = response.json()
        assert data["name"] == "Marco Alfaro"

    def test_create_user_returns_job(self):
        """Created user response should contain the submitted job"""
        payload = {"name": "Marco Alfaro", "job": "QA Engineer"}
        response = post("/users", payload)
        data = response.json()
        assert data["job"] == "QA Engineer"

    def test_create_user_returns_id(self):
        """Created user response should contain an auto-generated ID"""
        payload = {"name": "Marco Alfaro", "job": "QA Engineer"}
        response = post("/users", payload)
        data = response.json()
        assert "id" in data
        assert data["id"] is not None


class TestUpdateUser:

    def test_update_user_returns_200(self, existing_user_id):
        """PUT /users/{id} should return HTTP 200"""
        payload = {"name": "Marco Updated", "job": "Senior QA"}
        response = put(f"/users/{existing_user_id}", payload)
        assert response.status_code == 200

    def test_update_user_returns_updated_name(self, existing_user_id):
        """PUT response should reflect the updated name"""
        payload = {"name": "Marco Updated", "job": "Senior QA"}
        response = put(f"/users/{existing_user_id}", payload)
        data = response.json()
        assert data["name"] == "Marco Updated"

    def test_update_user_returns_updated_job(self, existing_user_id):
        """PUT response should reflect the updated job"""
        payload = {"name": "Marco Updated", "job": "Senior QA"}
        response = put(f"/users/{existing_user_id}", payload)
        data = response.json()
        assert data["job"] == "Senior QA"


class TestDeleteUser:

    def test_delete_user_returns_204(self, existing_user_id):
        """DELETE /users/{id} should return HTTP 204"""
        response = delete(f"/users/{existing_user_id}")
        assert response.status_code == 204

    def test_delete_user_returns_empty_body(self, existing_user_id):
        """DELETE response body should be empty"""
        response = delete(f"/users/{existing_user_id}")
        assert response.text == ""