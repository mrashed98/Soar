from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        """
        Initializes the BasePage class.
        :param driver: The WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def get_locator_strategy(self, selector):
        """
        Determine the appropriate locator strategy based on the selector format.
        Returns a tuple of (locator_type, locator_value)
        """
        if selector.startswith('@id/'):
            return (AppiumBy.ID, f"org.wikipedia.alpha:{selector[4:]}")
        elif selector.startswith('@content-desc='):
            return (AppiumBy.ACCESSIBILITY_ID, selector[13:])
        elif selector.startswith('//'):
            return (AppiumBy.XPATH, selector)
        elif selector.startswith('id='):
            return (AppiumBy.ID, selector[3:])
        else:
            return (AppiumBy.XPATH, selector)

    def find_element_with_timeout(self, selector, timeout=30):
        """
        Find an element using multiple strategies with timeout
        """
        locator_type, locator_value = self.get_locator_strategy(selector)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Element not found with {locator_type}: {locator_value}")
            print("Page source:", self.driver.page_source)
            raise

    def find_clickable_element(self, selector, timeout=30):
        """
        Find a clickable element using multiple strategies with timeout
        """
        locator_type, locator_value = self.get_locator_strategy(selector)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            print(f"Clickable element not found with {locator_type}: {locator_value}")
            print("Page source:", self.driver.page_source)
            raise

    def click(self, selector):
        """
        Click on an element
        """
        element = self.find_clickable_element(selector)
        element.click()

    def set_value(self, selector, value):
        """
        Set value to an element
        """
        element = self.find_element_with_timeout(selector)
        element.clear()
        element.send_keys(value)

    def is_element_present(self, selector, timeout=5):
        """
        Check if an element is present
        """
        try:
            self.find_element_with_timeout(selector, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def assert_element_displayed(self, selector):
        """
        Assert that an element is displayed
        """
        element = self.find_element_with_timeout(selector)
        assert element.is_displayed(), f"Element {selector} is not displayed"

    def assert_element_not_displayed(self, selector):
        """
        Assert that an element is not displayed
        """
        assert not self.is_element_present(selector), f"Element {selector} is unexpectedly displayed"
