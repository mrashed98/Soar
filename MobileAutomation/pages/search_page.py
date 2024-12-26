from pages.base_page import BasePage

class SearchPage(BasePage):
    """
    Search page class that contains all the methods and locators for the search functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        # Search input elements
        self.search_input = "//android.widget.AutoCompleteTextView[@resource-id='org.wikipedia.alpha:id/search_src_text']"
        self.search_close_btn = "//android.widget.ImageView[@content-desc='Clear query']"
        self.search_results = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_list_item_title']"
        self.back_button = "//android.widget.ImageButton[@content-desc='Navigate up']"

    def input_text_into_search_box(self, text):
        """
        Input text into search box
        """
        self.set_value(self.search_input, text)

    def clear_search_text(self):
        """
        Clear search text by clicking the close button
        """
        if self.is_element_present(self.search_close_btn):
            self.click(self.search_close_btn)

    def validate_search_results_displayed(self):
        """
        Validate that search results are displayed
        """
        self.assert_element_displayed(self.search_results)

    def validate_search_results_not_displayed(self):
        """
        Validate that search results are not displayed
        """
        self.assert_element_not_displayed(self.search_results)

    def go_back_to_home_page(self):
        """
        Click back button to return to home page
        """
        self.click(self.back_button)

    def get_search_results_count(self):
        """
        Get the number of search results displayed
        """
        try:
            elements = self.driver.find_elements_by_xpath(self.search_results)
            return len(elements)
        except:
            return 0

    def is_search_input_displayed(self):
        """
        Check if search input is displayed
        """
        return self.is_element_present(self.search_input)
