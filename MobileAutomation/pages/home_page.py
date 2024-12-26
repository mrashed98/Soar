from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Home page class that contains all the methods and locators for the home page functionality
    """

    def __init__(self, driver):
        super().__init__(driver)
        # Navigation menu locators
        self.my_lists_nav_menu = "//android.widget.FrameLayout[@content-desc='My lists']"
        self.history_nav_menu = "//android.widget.FrameLayout[@content-desc='History']"
        self.nearby_nav_menu = "//android.widget.FrameLayout[@content-desc='Nearby']"
        self.explore_nav_menu = "//android.widget.FrameLayout[@content-desc='Explore']"
        
        # Menu elements
        self.menu_button = "//android.support.v7.widget.LinearLayoutCompat//android.widget.TextView[@content-desc='More options' and @resource-id='org.wikipedia.alpha:id/menu_overflow_button']"
        self.settings_button = "//android.widget.TextView[@text='Settings']"
        
        # Search elements
        self.search_container = "//android.widget.LinearLayout[@resource-id='org.wikipedia.alpha:id/search_container']"
        self.search_input = "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/search_src_text']"
        self.search_results = "//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/page_list_item_title']"
        
        # Explore feed elements
        self.explore_feed = "//android.support.v7.widget.RecyclerView[@resource-id='org.wikipedia.alpha:id/fragment_feed_feed']"

    def is_displayed(self):
        """
        Verify that the home page is displayed by checking for the search container
        """
        return self.is_element_present(self.search_container)

    def click_on_menu_button(self):
        """
        Click on menu button
        """
        self.click(self.menu_button)

    def click_on_settings_button(self):
        """
        Click on settings button
        """
        self.click(self.settings_button)

    def open_my_lists_menu(self):
        """
        Open My Lists menu
        """
        self.click(self.my_lists_nav_menu)

    def open_history_menu(self):
        """
        Open History menu
        """
        self.click(self.history_nav_menu)

    def open_nearby_menu(self):
        """
        Open Nearby menu
        """
        self.click(self.nearby_nav_menu)

    def open_explore_menu(self):
        """
        Open Explore menu
        """
        self.click(self.explore_nav_menu)

    def click_on_search_container(self):
        """
        Click on search container to initiate search
        """
        self.click(self.search_container)

    def enter_search_text(self, text):
        """
        Enter text in search input
        """
        self.send_keys(self.search_input, text)

    def get_search_results(self):
        """
        Get list of search result titles
        """
        return self.find_elements(self.search_results)
