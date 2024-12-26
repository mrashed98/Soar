from .base_page import BasePage
from playwright.sync_api import Page

class ProductDialog(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self._dialog_container = ".mat-dialog-container"
        self._product_image = ".img-thumbnail"
        self._reviews_button = "[aria-label='Expand for Reviews']"
        self._reviews_section = ".mat-expansion-panel-content"
        self._close_dialog_button = "[aria-label='Close Dialog']"
        
    def is_dialog_visible(self) -> bool:
        """Check if product dialog is visible"""
        return self.is_visible(self._dialog_container)
        
    def is_product_image_visible(self) -> bool:
        """Check if product image is visible"""
        return self.is_visible(self._product_image)
                
    def expand_reviews(self):
        """Click on reviews button to expand reviews"""
        if self.is_visible(self._reviews_button):
            self.click(self._reviews_button)
            
    def is_reviews_expanded(self) -> bool:
        """Check if reviews section is expanded"""
        self.wait_for_element(self._reviews_section)
        return self.is_visible(self._reviews_section)
            
    def close_dialog(self):
        """Close the product dialog"""
        self.click(self._close_dialog_button)
    
    def wait_for_dialog(self):
        self.wait_for_element(self._dialog_container)
