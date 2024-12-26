import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
import time
import os

class TestWikipediaApp(unittest.TestCase):
    """
    Test class for validating menu navigation in the Wikipedia app.
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

    def test_validate_all_menu_navigation(self):
        """
        Validate navigation through all menu items.
        """
        try:
            # Wait for app to load and skip initial screens
            time.sleep(5)
            
            # Print current activity and package
            print(f"\nCurrent Activity: {self.driver.current_activity}")
            print(f"Current Package: {self.driver.current_package}")
            
            # Print page source for debugging
            print("\nPage Source:")
            print(self.driver.page_source)

            home_page = HomePage(self.driver)

            # Verify we're on the home page
            assert home_page.is_displayed(), "Home page is not displayed"

            home_page.click_on_menu_button()
            time.sleep(1)
            self.driver.back()

            # Open "My Lists" menu
            home_page.open_my_lists_menu()
            time.sleep(2)

            # Open "History" menu
            home_page.open_history_menu()
            time.sleep(2)

            # Open "Nearby" menu
            home_page.open_nearby_menu()
            time.sleep(2)

            # Open "Explore" menu
            home_page.open_explore_menu()
            time.sleep(2)

            # Final verification
            assert home_page.is_displayed(), "Home page is not displayed after navigation"

        except Exception as e:
            # Take screenshot on failure
            if hasattr(self, 'driver'):
                self.driver.save_screenshot('test_menu_navigation_error.png')
            print(f"\nError: {str(e)}")
            raise

if __name__ == '__main__':
    unittest.main()
