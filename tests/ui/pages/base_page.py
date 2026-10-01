class BasePage:

    def __init__(self, page):
        self.page = page

    def login(self, username="standard_user", password="secret_sauce"):
        """Navigate to login page and authenticate."""
        self.page.goto("https://www.saucedemo.com")
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()