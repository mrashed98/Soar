from math import log
from playwright.sync_api import Page
from utils.logger import log_action

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._welcome_banner = ".cdk-overlay-container mat-dialog-container"
        self._dismiss_button = "[aria-label='Close Welcome Banner']"
        self._me_want_it_button = ".cc-btn"
        
        
    @log_action
    def navigate(self, url: str):
        """Navigate to the specified URL"""
        self.page.goto(url)
        
    @log_action 
    def get_title(self) -> str:
        """Get the page title"""
        return self.page.title()
    
    @log_action
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for an element to be visible"""
        return self.page.wait_for_selector(selector, timeout=timeout)
    
    @log_action
    def click(self, selector: str):
        """Click on an element"""
        self.page.click(selector)
        
    @log_action
    def fill(self, selector: str, value: str):
        """Fill a form field"""
        self.page.fill(selector, value)
    
    @log_action
    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        return self.page.text_content(selector)
    
    @log_action
    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible"""
        return self.page.is_visible(selector)

    @log_action
    def dismiss_welcome_banner(self):
        """Dismiss the welcome banner if present"""
        self.wait_for_element(self._welcome_banner)
        try:
            if self.is_visible(self._welcome_banner):
                self.click(self._dismiss_button)
        except:
            pass
    @log_action        
    def accept_cookies(self):
        """Accept cookies if the banner is present"""
        self.wait_for_element(self._me_want_it_button)
        try:
            if self.is_visible(self._me_want_it_button):
                self.click(self._me_want_it_button)
        except:
            pass

    @log_action
    def fill_numeric_field(self, selector: str, value: int):
        """Fill a numeric field"""
        number_input = self.page.locator(selector)
        number_input.type(str(value))