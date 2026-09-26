import pytest
from tests.ui.pages.login_page import LoginPage


class TestLogin:

    @pytest.mark.smoke
    def test_valid_login_redirects_to_inventory(self, page):
        """Valid credentials should redirect to /inventory.html"""
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        assert page.url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.smoke
    def test_valid_login_shows_products(self, page):
        """After login, product list should be visible"""
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        assert page.locator(".inventory_list").is_visible()

    @pytest.mark.regression
    def test_invalid_password_shows_error(self, page):
        """Wrong password should display an error message"""
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "wrong_password")
        error = login.get_error_message()
        assert "Username and password do not match" in error

    @pytest.mark.regression
    def test_empty_username_shows_error(self, page):
        """Empty username should display an error message"""
        login = LoginPage(page)
        login.navigate()
        login.login("", "secret_sauce")
        error = login.get_error_message()
        assert "Username is required" in error

    @pytest.mark.regression
    def test_locked_user_shows_error(self, page):
        """Locked out user should display specific error message"""
        login = LoginPage(page)
        login.navigate()
        login.login("locked_out_user", "secret_sauce")
        error = login.get_error_message()
        assert "locked out" in error