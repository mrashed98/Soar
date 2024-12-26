from this import d
from .base_page import BasePage
from playwright.sync_api import expect, Page
import logging

logging.basicConfig(level=logging.INFO)

class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Input fields
        self._email_input = "#emailControl"
        self._password_input = "#passwordControl"
        self._repeat_password_input = "#repeatPasswordControl"
        self._security_question_select = "[name='securityQuestion']"
        self._show_password_advice = '//mat-slide-toggle[contains(., "Show password advice")]'
        self._password_advice_content = 'mat-password-strength-info .mat-card-content'
        self._security_answer_input = "#securityAnswerControl"
        self._register_button = "#registerButton"
        
        # Error message selectors
        self._email_error = "#mat-error-0"
        self._password_error = "#mat-error-1"
        self._repeat_password_error = "#mat-error-2"
        self._security_answer_error = "#mat-error-4"
        self._security_question_error = "#mat-error-3"
        

        #Success message selectors
        self._success_message = 'Registration completed successfully. You can now log in.'

    
        
    def click_email_field(self):
        """Click email field"""
        self.click(self._email_input)

    def click_password_field(self):
        """Click password field"""
        self.click(self._password_input)

    def click_repeat_password_field(self):
        """Click repeat password field"""
        self.click(self._repeat_password_input)

    def click_show_password_advice(self):
        """Click show password advice"""
        self.click(self._show_password_advice)
        self.wait_for_element(self._password_advice_content)
        self.page.wait_for_timeout(4000)

    def click_security_question(self):
        """Click security question select"""
        self.click(self._security_question_select)


    def click_security_answer_field(self):
        """Click security answer field"""
        self.click(self._security_answer_input)

    def click_register(self):
        """Click register button"""
        self.click(self._register_button)
        self.page.wait_for_timeout(4000)

    def dismiss_security_question_field(self):
        """Dismiss security question select"""
        self.page.keyboard.press("Escape")

    def move_to_next_field(self):
        """Move to next field"""
        self.page.keyboard.press("Tab")


    def select_security_question(self, question_index: int):
        """Select security question by index"""
        self.click(self._security_question_select)
        self.page.keyboard.press(f"ArrowDown")
        for _ in range(question_index):
            self.page.keyboard.press(f"ArrowDown")
        self.page.keyboard.press("Enter")

    def fill_email(self, email: str):
        """Fill email field and trigger validation"""
        self.fill(self._email_input, email)
        # Click outside to trigger validation
        self.move_to_next_field()
        
    def fill_password(self, password: str):
        """Fill password field and trigger validation"""
        self.fill(self._password_input, password)
        # Click outside to trigger validation
        self.move_to_next_field()
        
    def fill_repeat_password(self, password: str):
        """Fill repeat password field and trigger validation"""
        self.fill(self._repeat_password_input, password)
        # Click outside to trigger validation
        self.move_to_next_field()
        
    def fill_security_answer(self, answer: str):
        """Fill security answer field and trigger validation"""
        self.fill(self._security_answer_input, answer)
        # Click outside to trigger validation
        self.move_to_next_field()
        
        
    def is_email_field_error_message_visible(self) -> bool:
        """Check if email error message is visible after interaction"""
        return self.is_visible(self._email_error)
        
    def is_password_field_error_message_visible(self) -> bool:
        """Check if password error message is visible after interaction"""
        return self.is_visible(self._password_error)
        
    def is_repeat_password_field_error_message_visible(self) -> bool:
        """Check if repeat password error message is visible after interaction"""
        return self.is_visible(self._repeat_password_error)
        
    def is_security_question_field_error_message_visible(self) -> bool:
        """Check if security question error message is visible after interaction"""
        return self.is_visible(self._security_question_error)   

    def is_security_answer_field_error_message_visible(self) -> bool:
        """Check if security answer error message is visible after interaction"""
        return self.is_visible(self._security_answer_error)
        
    def is_success_message_visible(self) -> bool:
        """Is success message visible"""
        success_message = self.page.get_by_text(self._success_message)
        return success_message.is_visible()

    def get_email_error_message(self) -> str:
        """Get email error message text"""
        return self.get_text(self._email_error) if self.is_email_field_error_message_visible() else ""
        
    def get_password_error_message(self) -> str:
        """Get password error message text"""
        return self.get_text(self._password_error) if self.is_password_field_error_message_visible() else ""
        
    def get_repeat_password_error_message(self) -> str:
        """Get repeat password error message text"""
        return self.get_text(self._repeat_password_error) if self.is_repeat_password_field_error_message_visible() else ""
        
    def get_security_question_error_message(self) -> str:
        """Get security question error message text"""
        return self.get_text(self._security_question_error) if self.is_security_question_field_error_message_visible() else ""

    def get_security_answer_error_message(self) -> str:
        """Get security answer error message text"""
        return self.get_text(self._security_answer_error) if self.is_security_answer_field_error_message_visible() else ""

    