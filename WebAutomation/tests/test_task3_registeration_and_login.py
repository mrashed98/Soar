import pytest
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from config.test_data import TestData


def test_registration_field_validations(page: Page):
    """Test registration form field validations"""
    register_page = RegisterPage(page)
    
    # Navigate to registration page
    page.goto(TestData.REGISTERATION_URL)

    register_page.dismiss_welcome_banner()
    register_page.accept_cookies()
    
    register_page.click_email_field()
    register_page.click_password_field()
    register_page.click_repeat_password_field()
    register_page.click_security_question()
    register_page.dismiss_security_question_field()
    register_page.click_security_answer_field()
    register_page.move_to_next_field()
    
    assert register_page.is_email_field_error_message_visible(), "Email error should be visible"
    assert "email address" in register_page.get_email_error_message().lower()
    assert register_page.is_password_field_error_message_visible(), "Password error should be visible"
    assert "password" in register_page.get_password_error_message().lower()
    assert register_page.is_repeat_password_field_error_message_visible(), "Repeat password error should be visible"
    assert "repeat" in register_page.get_repeat_password_error_message().lower()
    assert register_page.is_security_question_field_error_message_visible(), "Security question error should be visible"
    assert "security" in register_page.get_security_question_error_message().lower()
    assert register_page.is_security_answer_field_error_message_visible(), "Security answer error should be visible"
    assert "answer" in register_page.get_security_answer_error_message().lower()
    
def test_successful_registration(page: Page):
    """Test successful registration"""
    register_page = RegisterPage(page)
    
    # Navigate to registration page
    page.goto(TestData.REGISTERATION_URL)

    register_page.dismiss_welcome_banner()
    register_page.accept_cookies()
    
    register_page.fill_email(TestData.EMAIL)
    register_page.fill_password(TestData.PASSWORD)
    register_page.fill_repeat_password(TestData.PASSWORD)
    register_page.click_show_password_advice()
    register_page.select_security_question(0)
    register_page.fill_security_answer(TestData.SECURITY_ANSWER)
    register_page.click_register()
    
    assert page.url == TestData.LOGIN_URL, "User should be redirected to login page"
    assert register_page.is_success_message_visible(), "Success message should be visible"


def test_login_after_registration(page: Page):
    """Test login after successful registration"""
    login_page = LoginPage(page)
    login_page.navigate(TestData.LOGIN_URL)
    login_page.login(TestData.EMAIL, TestData.PASSWORD)
    
    assert login_page.is_logged_in(), "User should be logged in"