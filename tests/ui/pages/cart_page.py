class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def get_item_count(self):
        """Return number of items currently in cart."""
        try:
            self.page.wait_for_selector(".cart_item", timeout=3000)
        except Exception:
            return 0
        return self.cart_items.count()

    def get_item_names(self):
        """Return list of product names in cart."""
        self.page.wait_for_selector(".inventory_item_name", timeout=10000)
        return self.cart_items.locator(".inventory_item_name").all_text_contents()

    def remove_item(self, item_name):
        """Remove a specific item from cart by name."""
        item = self.page.locator(f".cart_item:has-text('{item_name}')")
        item.locator("button").click()