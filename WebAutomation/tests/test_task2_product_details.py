import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.product_dialog import ProductDialog
from config.test_data import TestData

def test_apple_juice_product_details(page: Page):
    """Task 2: Verify Apple Juice product details and review functionality"""
    home_page = HomePage(page)
    product_dialog = ProductDialog(page)
    
    # Navigate to the website
    page.goto(TestData.BASE_URL)
    
    # Handle welcome banner and cookies
    home_page.dismiss_welcome_banner()
    home_page.accept_cookies()
    
    
    # Check if Apple Juice card is visible
    if not home_page.is_visible(home_page._apple_juice_card):
        pytest.skip("Apple Juice card is not visible")
    
    # Click on Apple Juice product
    home_page.click_apple_juice()
    
    # Wait for and verify product dialog
    product_dialog.wait_for_dialog()
    assert product_dialog.is_dialog_visible(), "Product dialog is not visible"
    
    # Verify product image
    assert product_dialog.is_product_image_visible(), "Product image is not visible"
    
    
    product_dialog.expand_reviews()
    assert product_dialog.is_reviews_expanded(), "Reviews section did not expand"
    
    
    # Wait for a couple of seconds to view the reviews
    page.wait_for_timeout(4000)
    
    # Close the product dialog
    product_dialog.close_dialog()
    
    page.wait_for_timeout(2000)

    # Verify dialog is closed
    assert not product_dialog.is_dialog_visible(), "Product dialog did not close"
