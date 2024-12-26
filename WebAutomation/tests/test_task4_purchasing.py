import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from config.test_data import TestData


def test_purchasing(page: Page):
    """Test purchasing"""
    home_page = HomePage(page)
    basket_page = BasketPage(page)
    login_page = LoginPage(page)

    # Navigate to the website
    login_page.navigate(TestData.LOGIN_URL)

    # Login
    login_page.login(TestData.EMAIL, TestData.PASSWORD)

    home_page.dismiss_welcome_banner()
    home_page.accept_cookies()

    # Add a product to the basket
    home_page.add_product_to_basket(5)
    
    assert home_page.get_total_items_in_basket() == 5, "Not all Items added to basket"

    # Click on the basket
    basket_page.click_shopping_cart()
    total_price = basket_page.get_total_price()

    basket_page.add_quantity()
    basket_page.add_quantity()
    basket_page.remove_quantity()
    basket_page.remove_quantity()
    basket_page.delete_product()

    assert basket_page.get_total_price() < total_price, "Total price is not changed after deleting the product"
    
    assert basket_page.place_order(), "Order is not placed"




    