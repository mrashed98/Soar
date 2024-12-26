import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
from pages.search_page import SearchPage
import time
import os

class TestWikipediaSearch(unittest.TestCase):
    """
    Test class for validating search functionality in the Wikipedia app.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        # Get the absolute path to the APK file
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        apk_path = os.path.join(current_dir, 'apk', 'WikipediaSample.apk')

        # Set up Appium options
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.app = apk_path
        options.device_name = 'emulator-5554'
        options.app_package = 'org.wikipedia.alpha'
        options.app_activity = 'org.wikipedia.main.MainActivity'
        options.no_reset = True
        options.auto_grant_permissions = True

        # Connect to Appium server
        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
            self.driver.implicitly_wait(30)
        except Exception as e:
            print(f"Failed to connect to Appium server: {str(e)}")
            raise

    def tearDown(self):
        """
        Clean up the test environment after each test case.
        """
        if hasattr(self, 'driver'):
            try:
                self.driver.quit()
            except:
                pass

    def test_validate_search_functionality(self):
        """
        Validate the search functionality.
        """
        try:
            # Wait for app to load
            time.sleep(5)

            # Print current activity and package
            print(f"\nCurrent Activity: {self.driver.current_activity}")
            print(f"Current Package: {self.driver.current_package}")

            # Initialize page objects
            home_page = HomePage(self.driver)
            search_page = SearchPage(self.driver)

            # Verify we're on the home page
            assert home_page.is_displayed(), "Home page is not displayed"

            # Click on the search container
            home_page.click_on_search_container()
            time.sleep(2)

            # Verify search input is displayed
            assert search_page.is_search_input_displayed(), "Search input is not displayed"

            # Enter search text
            search_page.input_text_into_search_box('New York')
            time.sleep(2)

            # Validate search results displayed
            search_page.validate_search_results_displayed()

            # Get and print the number of search results
            results_count = search_page.get_search_results_count()
            print(f"\nNumber of search results: {results_count}")

            # Clear search text
            search_page.clear_search_text()
            time.sleep(2)

            # Validate search results not displayed
            search_page.validate_search_results_not_displayed()

            # Go back to home page
            search_page.clear_search_text()
            time.sleep(2)

            # Final verification
            assert home_page.is_displayed(), "Home page is not displayed after search"

        except Exception as e:
            # Take screenshot on failure
            if hasattr(self, 'driver'):
                self.driver.save_screenshot('test_search_error.png')
            print(f"\nError: {str(e)}")
            raise

if __name__ == '__main__':
    unittest.main()
