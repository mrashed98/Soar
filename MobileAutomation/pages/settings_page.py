from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SettingsPage(BasePage):
    """
    Settings page class that contains all the methods and locators for the settings functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        # Settings elements
        self.settings_title = "//android.widget.TextView[@text='Settings']"
        self.about_wikipedia_button = "//android.widget.TextView[@text='About the Wikipedia app' and @resource-id='android:id/title']"
        self.privacy_policy_button = "//android.widget.TextView[@text='Privacy policy' and @resource-id='android:id/title']"
        self.terms_of_use_button = "//android.widget.TextView[@text='Terms of use' and @resource-id='android:id/title']"
        self.back_button = "//android.widget.ImageButton[@content-desc='Navigate up']"
        
        # Toggle switches
        self.all_switches = "//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget']"
        self.show_images_switch = "//android.widget.TextView[@text='Show images']/../following-sibling::android.widget.LinearLayout//android.widget.Switch"
        self.show_link_previews_switch = "//android.widget.TextView[@text='Show link previews']/../following-sibling::android.widget.LinearLayout//android.widget.Switch"
        self.send_usage_reports_switch = "//android.widget.TextView[@text='Send usage reports']/../following-sibling::android.widget.LinearLayout//android.widget.Switch"
        self.send_crash_reports_switch = "//android.widget.TextView[@text='Send crash reports']/../following-sibling::android.widget.LinearLayout//android.widget.Switch"
        
        # About page elements
        self.about_page_title = "//android.widget.TextView[@text='About']"
        self.app_version_text = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/about_version_text']"
        self.contributors_link = "//android.widget.TextView[@text='Contributors']"
        self.translators_link = "//android.widget.TextView[@text='Translators']"
        self.licenses_link = "//android.widget.TextView[@text='License']"

    def toggle_all_switches(self):
        """
        Toggle all switches in settings to OFF
        """
        switches = self.driver.find_elements(By.XPATH, self.all_switches)
        for switch in switches:
            if switch.get_attribute("checked") == "true":
                switch.click()

    def verify_all_switches_off(self):
        """
        Verify all switches are turned OFF
        """
        switches = self.driver.find_elements(By.XPATH, self.all_switches)
        return all(switch.get_attribute("checked") == "false" for switch in switches)

    def click_about_wikipedia(self):
        """
        Click on About Wikipedia button
        """
        self.click(self.about_wikipedia_button)

    def click_privacy_policy(self):
        """
        Click on Privacy Policy button
        """
        self.click(self.privacy_policy_button)

    def click_terms_of_use(self):
        """
        Click on Terms of Use button
        """
        self.click(self.terms_of_use_button)

    def go_back(self):
        """
        Click back button to return to previous page
        """
        self.click(self.back_button)

    def is_settings_page_displayed(self):
        """
        Check if settings page is displayed
        """
        return self.is_element_present(self.settings_title)

    def is_about_page_displayed(self):
        """
        Check if about page is displayed
        """
        return self.is_element_present(self.about_page_title)

    def get_app_version(self):
        """
        Get the app version text
        """
        try:
            version_element = self.find_element(self.app_version_text)
            return version_element.text
        except:
            return None

    def verify_about_page_links(self):
        """
        Verify that all links in the about page are present
        """
        links = [
            self.contributors_link,
            self.translators_link,
            self.licenses_link
        ]
        return all(self.is_element_present(link) for link in links)
