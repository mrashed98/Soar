from .base_page import BasePage
from playwright.sync_api import Page
from config.test_data import TestData
from utils.logger import log_action
import logging


class BasketPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Basked Locators
        self._shopping_cart = '[aria-label="Show the shopping cart"]'
        self._total_price = "#price"
        self._add_quantity_icon = '//mat-row[1]//mat-cell[contains(@class, "mat-column-quantity")]//*[contains(@class, "plus-square")]'
        self._remove_quantity_icon = '//mat-row[1]//mat-cell[contains(@class, "mat-column-quantity")]//*[contains(@class, "minus-square")]'
        self._checkout_button = '#checkoutButton'
        self._delete_button = '[data-icon="trash-alt"]'

        # Address Locators
        self._add_new_address_button = '[aria-label="Add a new address"]'
        self._country_Input = '[data-placeholder="Please provide a country."]'
        self._name_Input = '[data-placeholder="Please provide a name."]'
        self._mobile_Input = '[data-placeholder="Please provide a mobile number."]'
        self._address_input = '[data-placeholder="Please provide an address."]'
        self._city_Input = '[data-placeholder="Please provide a city."]'
        self._state_Input = '[data-placeholder="Please provide a state."]'
        self._zip_Input = '[data-placeholder="Please provide a ZIP code."]'
        self._address_submit_button = '#submitButton'
        self._address_row = 'app-address-select mat-row'

        # Payment Locators
        self._proceed_to_payment_button = '[aria-label="Proceed to delivery method selection"]'
        self._delivery_method_row = 'app-delivery-method mat-row'
        self._proceed_to_delivery_button = '[aria-label="Proceed to payment selection"]'
        self._wallet_balance = '#walletBalance'

        self._add_new_card_button = '#mat-expansion-panel-header-9'
        self._card_name = 'Name *'
        self._card_number_Input = 'Card Number *'
        self._card_expiry_month_dropdown = 'Expiry Month *'
        self._card_expiry_year_dropdown = 'Expiry Year *'
        self._save_card_info_button = '#submitButton'

        self._payment_method_row = 'app-payment-method mat-row mat-radio-button'
        
        self._proceed_to_review_button = '[aria-label="Proceed to review"]'
        self._complete_your_purchase_button = '#completeYourPurchaseButton'
        self._order_success_message = 'Thank you for your purchase!'


    @log_action
    def click_shopping_cart(self):
        self.click(self._shopping_cart)
        self.page.wait_for_url(TestData.BASKET_URL, timeout=5000)

    @log_action
    def get_total_price(self):
        self.page.wait_for_selector(self._total_price)
        self.page.wait_for_timeout(2000)
        total_price = self.get_text(self._total_price)
        current_price = float(total_price.replace('Total Price: ', '').replace('¤', ''))
        logger = logging.getLogger('playwright_tests')
        logger.info(f"Total price retrieved: {current_price}")
        return current_price

    @log_action
    def add_quantity(self):
        self.click(self._add_quantity_icon)

    @log_action
    def remove_quantity(self):
        self.click(self._remove_quantity_icon)

    @log_action
    def delete_product(self):
        self.click(self._delete_button)
        self.page.wait_for_timeout(4000)

    @log_action
    def click_checkout_button(self):
        self.click(self._checkout_button)

    @log_action
    def click_add_new_address_button(self):
        self.page.wait_for_selector(self._add_new_address_button)
        self.click(self._add_new_address_button)

    @log_action
    def add_new_address(self):
        self.fill(self._country_Input, TestData.ADDRESS["country"])
        self.fill(self._name_Input, TestData.ADDRESS["name"])
        self.fill_numeric_field(self._mobile_Input, TestData.ADDRESS["mobile"])
        self.fill(self._address_input, TestData.ADDRESS["address"])
        self.fill(self._city_Input, TestData.ADDRESS["city"])
        self.fill(self._state_Input, TestData.ADDRESS["state"])
        self.fill_numeric_field(self._zip_Input, TestData.ADDRESS["zip"])
        self.click(self._address_submit_button)

    @log_action
    def select_address_row(self):
        self.wait_for_element(self._address_row)
        self.page.locator(self._address_row).nth(0).click()

    @log_action
    def select_delivery_method(self):
        self.wait_for_element(self._delivery_method_row)
        self.page.locator(self._delivery_method_row).nth(0).click()

    @log_action
    def proceed_to_delivery(self):
        self.wait_for_element(self._proceed_to_delivery_button)
        self.click(self._proceed_to_delivery_button)

    @log_action
    def proceed_to_payment(self):
        self.wait_for_element(self._proceed_to_payment_button)
        self.click(self._proceed_to_payment_button)

    @log_action
    def select_payment_method(self):
        self.page.wait_for_selector(self._payment_method_row)
        self.click(self._payment_method_row)

    @log_action
    def proceed_to_review(self):
        self.wait_for_element(self._proceed_to_review_button)
        self.click(self._proceed_to_review_button)

    @log_action
    def get_wallet_balance(self):
        return self.get_text(self._wallet_balance)

    @log_action
    def click_add_new_card_button(self):
        self.page.get_by_text('Add new card').click()

    @log_action
    def add_new_card(self):
        card_name = self.page.get_by_label(self._card_name)
        card_name.fill("Test Card")

        card_number = self.page.get_by_label(self._card_number_Input)
        card_number.type(TestData.CARD["cardNumber"])

        card_expirty_month = self.page.get_by_label(self._card_expiry_month_dropdown)
        card_expirty_month.type(TestData.CARD["cardExpiryMonth"])
        
        card_expiry_year = self.page.get_by_label(self._card_expiry_year_dropdown)
        card_expiry_year.type(TestData.CARD["cardExpiryYear"])
        self.click(self._save_card_info_button)

    @log_action
    def place_order(self):
        logger = logging.getLogger('playwright_tests')
        logger.info("Starting order placement")
        
        self.click_checkout_button()
        logger.info("Clicked checkout")
        
        self.click_add_new_address_button()
        self.add_new_address()
        logger.info("Added new address")

        logger.info("Selecting address row")
        self.select_address_row()

        logger.info("Selecting address row")
        self.proceed_to_delivery()
        self.select_delivery_method()

        logger.info("Proceeding to payment")
        self.proceed_to_payment()

        logger.info("Adding new card")
        self.click_add_new_card_button()
        self.add_new_card()
        self.select_payment_method()

        logger.info("Proceeding to review")
        self.proceed_to_review()

        logger.info("Completing purchase")
        self.click_checkout_button()

        self.page.wait_for_timeout(2000)

        success_message = self.page.get_by_text(self._order_success_message)
        logger.info(f"Order placement completed")
        return success_message.is_visible()