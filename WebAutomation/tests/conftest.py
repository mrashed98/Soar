import pytest
from playwright.sync_api import sync_playwright
import logging
import os
from datetime import datetime

def setup_logging():
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(logs_dir, exist_ok=True)

    # Generate unique log filename with timestamp and run number
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(logs_dir, f'test_run_{timestamp}.log')

    # Configure logging
    logger = logging.getLogger('playwright_tests')
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize logger
logger = setup_logging()

def pytest_configure(config):
    """Configure pytest with custom markers and logging setup"""
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")

@pytest.fixture(scope="session")
def browser():
    logger.info("Starting browser session")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        logger.info("Browser launched successfully")
        yield browser
        logger.info("Closing browser session")
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    logger.info("Creating new browser context and page")
    context = browser.new_context()
    page = context.new_page()
    logger.info("New page created")
    yield page
    logger.info("Closing browser context and page")
    context.close()
