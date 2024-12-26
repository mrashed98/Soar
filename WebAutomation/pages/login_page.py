from .base_page import BasePage
from playwright.sync_api import Page
from config.test_data import TestData

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self._email_input = "#email"
        self._password_input = "#password"
        self._login_button = "#loginButton"
        self._error_message = ".error"
        self._remember_me = "#rememberMe"
        
    def login(self, email: str, password: str, remember_me: bool = False):
        """Perform login with given credentials"""
        self.page.wait_for_url(TestData.LOGIN_URL, timeout=5000)
        self.fill(self._email_input, email)
        self.fill(self._password_input, password)
        if remember_me:
            self.click(self._remember_me)
        self.click(self._login_button)
        self.page.wait_for_url(f"{TestData.HOME_URL}search", timeout=5000)
        
    def get_error_message(self) -> str:
        """Get login error message if present"""
        return self.get_text(self._error_message)
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in"""
        return not self.is_visible(self._login_button)
