import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from config.test_data import TestData
from utils.logger import log_action
import logging

def test_display_all_items(page: Page):
    """Test displaying all items and verifying count"""
    home_page = HomePage(page)
    
    logger = logging.getLogger('playwright_tests')
    logger.info("Starting product listing test")
    
    page.goto(TestData.BASE_URL)
    logger.info("Navigated to base URL")
    
    home_page.dismiss_welcome_banner()
    home_page.accept_cookies()
    
    initial_count = home_page.get_displayed_items_count()
    logger.info(f"Initial items count: {initial_count}")
    
    home_page.set_items_per_page()
    logger.info("Changed items per page")
    
    final_count = home_page.get_displayed_items_count()
    logger.info(f"Final items count: {final_count}")
    
    assert final_count > initial_count
