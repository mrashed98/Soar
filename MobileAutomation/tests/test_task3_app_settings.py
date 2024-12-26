import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
import time
import os

class TestWikipediaSettings(unittest.TestCase):
    """
    Test class for validating settings functionality in the Wikipedia app.
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

    def test_validate_settings_functionality(self):
        """
        Validate the settings functionality:
        1. Navigate to settings
        2. Toggle all switches to OFF
        3. Verify all switches are OFF
        4. Navigate to About page
        5. Verify About page elements
        6. Return to home page
        """
        try:
            # Wait for app to load
            time.sleep(5)

            # Print current activity and package
            print(f"\nCurrent Activity: {self.driver.current_activity}")
            print(f"Current Package: {self.driver.current_package}")

            # Initialize page objects
            home_page = HomePage(self.driver)
            settings_page = SettingsPage(self.driver)

            # Verify we're on the home page
            assert home_page.is_displayed(), "Home page is not displayed"

            # Navigate to settings
            home_page.click_on_menu_button()
            time.sleep(1)
            home_page.click_on_settings_button()
            time.sleep(2)

            # Verify we're on the settings page
            assert settings_page.is_settings_page_displayed(), "Settings page is not displayed"

            # Toggle all switches to OFF
            settings_page.toggle_all_switches()
            time.sleep(2)

            # Verify all switches are OFF
            assert settings_page.verify_all_switches_off(), "Not all switches are turned OFF"

            # Click on About Wikipedia
            settings_page.click_about_wikipedia()
            time.sleep(2)

            # Verify we're on the about page
            assert settings_page.is_about_page_displayed(), "About page is not displayed"

            # Get and print app version
            app_version = settings_page.get_app_version()
            if app_version:
                print(f"\nApp Version: {app_version}")

            # Verify about page links
            assert settings_page.verify_about_page_links(), "Not all about page links are present"

            # Go back to settings page
            settings_page.go_back()
            time.sleep(1)

            # Verify back on settings page
            assert settings_page.is_settings_page_displayed(), "Settings page is not displayed after going back"

            # Go back to home page
            settings_page.go_back()
            time.sleep(1)

            # Final verification
            assert home_page.is_displayed(), "Home page is not displayed after settings"

        except Exception as e:
            # Take screenshot on failure
            if hasattr(self, 'driver'):
                self.driver.save_screenshot('test_settings_error.png')
                print(f"\nPage source: {self.driver.page_source}")
            print(f"\nError: {str(e)}")
            raise

if __name__ == '__main__':
    unittest.main()
