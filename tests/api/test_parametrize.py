import pytest
from utils.api_client import get, post

class TestParametrize:
    @pytest.mark.regression
    @pytest.mark.parametrize("page", [1, 2])
    def test_get_users_all_pages_returns_200(self, page):
        """GET /users should return 200 for all valid pages"""
        response = get("/users", params={"page": page})
        assert response.status_code == 200

    @pytest.mark.regression
    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
    def test_get_individual_users_returns_200(self, user_id):
        """GET /users/{id} should return 200 for all valid user IDs"""
        response = get(f"/users/{user_id}")
        assert response.status_code == 200

    @pytest.mark.regression
    @pytest.mark.parametrize("user_id", [9998, 9999])
    def test_invalid_user_ids_return_404(self, user_id):
        """GET /users/{id} should return 404 for non-existing IDs"""
        response = get(f"/users/{user_id}")
        assert response.status_code == 404

    @pytest.mark.regression
    @pytest.mark.parametrize("payload, expected_status", [
                                         ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200), 
                                                ({"email": "eve.holt@reqres.in"}, 400), 
                                                ({"password": "cityslicka"}, 400), 
                                        ])
    def test_login_scenarios(self, payload, expected_status):
        """POST /login should return correct status for each scenario"""
        response = post("/login", payload)
        assert response.status_code == expected_status

    