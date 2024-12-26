from math import e
from .base_page import BasePage
from playwright.sync_api import Page, expect
import logging
from utils.logger import log_action

logging.basicConfig(level=logging.DEBUG)


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self._items_per_page_select = '[aria-label*="Items per page"]'
        self._items_per_page_last_child = '[aria-label*="Items per page"] mat-option:last-child'
        self._items_range = ".mat-paginator-range-label"
        self._product_grid = "mat-grid-list"
        self._product_cards = "mat-grid-tile"
        self._apple_juice_card = "//mat-grid-tile//div[contains(text(), 'Apple Juice')]"
        self._success_message = "snack-bar-container"
        self._add_to_basket_button = 'mat-grid-tile button[aria-label="Add to Basket"]'
        self._shopping_cart = '[aria-label="Show the shopping cart"]'
        
    @log_action
    def scroll_to_bottom(self):
        """Scroll to the bottom of the page"""
        logging.debug("Scrolling to the bottom of the page")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
    @log_action
    def set_items_per_page(self):
        """Change the items per page count"""
        logging.debug("Changing items per page")
        self.page.locator(self._items_per_page_select).click()
        self.page.locator(self._items_per_page_last_child).click()
        
    @log_action
    def get_products_count(self) -> int:
        """Get the total number of products on the page"""
        logging.debug("Getting total number of products")
        return int(self.page.locator(self._items_range).text_content().strip().split(" ")[-1])

    @log_action
    def get_displayed_items_count(self) -> int:
        """Get the number of items displayed on the page"""
        logging.debug("Getting number of displayed items")
        return len(self.page.locator(self._product_cards).all())
    
    @log_action
    def click_apple_juice(self):
        """Click on the Apple Juice product"""
        logging.debug("Clicking on Apple Juice product")
        self.page.locator(self._apple_juice_card).click()

    @log_action
    def add_product_to_basket(self, count: int):
        """Add a product to the basket"""
        logging.debug("Adding product to basket")
        add_to_basket_buttons = self.page.locator(self._add_to_basket_button)
        total_items_in_basket = self.get_total_items_in_basket()
        i = 0
        while total_items_in_basket != count:
            add_to_basket_buttons.nth(i).click()
            expect(self.page.locator(self._success_message)).to_be_visible()
            self.page.wait_for_timeout(1000)
            total_items_in_basket = self.get_total_items_in_basket()
            i += 1
    @log_action
    def get_total_items_in_basket(self):
        """Get the total number of items in the basket"""
        logging.debug("Getting total items in the basket")
        return int(self.page.locator(self._shopping_cart).locator("span").locator("span:nth-child(3)").text_content())