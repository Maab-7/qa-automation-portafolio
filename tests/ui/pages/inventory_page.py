class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        self.page = page
        self.inventory_list = page.locator(".inventory_list")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_item_to_cart(self, item_name):
        """Add a specific product to cart by name."""
        self.page.wait_for_selector(f".inventory_item:has-text('{item_name}')")
        item = self.page.locator(f".inventory_item:has-text('{item_name}')")
        item.locator("button").click()

    def get_cart_count(self):
        """Return the number shown on the cart badge."""
        return self.cart_badge.text_content()

    def go_to_cart(self):
        """Click the cart icon to navigate to cart page."""
        self.cart_link.click()
        self.page.wait_for_url("**/cart.html")
        self.page.wait_for_load_state("networkidle")
        