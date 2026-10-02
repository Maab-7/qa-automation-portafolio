import pytest
from tests.ui.pages.base_page import BasePage
from tests.ui.pages.inventory_page import InventoryPage
from tests.ui.pages.cart_page import CartPage


class TestInventory:

    @pytest.mark.smoke
    def test_inventory_page_loads(self, page):
        """Inventory page should display product list after login."""
        BasePage(page).login()
        inventory = InventoryPage(page)
        page.wait_for_selector(".inventory_list")
        assert inventory.inventory_list.is_visible()

    @pytest.mark.smoke
    def test_add_single_item_updates_cart_badge(self, page):
        """Adding one item should show badge count of 1."""
        BasePage(page).login()
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        assert inventory.get_cart_count() == "1"

    @pytest.mark.regression
    def test_add_two_items_updates_cart_badge(self, page):
        """Adding two items should show badge count of 2."""
        BasePage(page).login()
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")
        assert inventory.get_cart_count() == "2"

    @pytest.mark.regression
    def test_added_item_appears_in_cart(self, page):
        """Item added from inventory should appear in cart."""
        BasePage(page).login()
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()
        cart = CartPage(page)
        assert "Sauce Labs Backpack" in cart.get_item_names()

    @pytest.mark.regression
    def test_remove_item_from_cart(self, page):
        """Removing item from cart should leave cart empty."""
        BasePage(page).login()
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()
        cart = CartPage(page)
        cart.remove_item("Sauce Labs Backpack")
        assert cart.get_item_count() == 0

    @pytest.mark.regression
    def test_cart_shows_correct_item_count(self, page):
        """Cart page should show same number of items as added."""
        BasePage(page).login()
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")
        inventory.go_to_cart()
        cart = CartPage(page)
        assert cart.get_item_count() == 2