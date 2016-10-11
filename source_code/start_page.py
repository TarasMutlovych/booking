from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver.common.by import By
from  .user_personal_page import UserPersonalPage


class StartPage(BasePage):

    SIGN_IN_BUTTON = (By.XPATH, ".//li[@id = 'current_account'][position() = 2]//div")
    EMAIL_INPUT = (By.CLASS_NAME, "user_access_email")
    PASSWORD_INPUT = (By.CLASS_NAME, "user_access_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "div.form-shown-section form.user_access_form-user_avatar--circle input[type = 'submit']")

    def _get_sign_in_button (self):
        return self.wait_for_element_visibility_located_by(locator= self.SIGN_IN_BUTTON)

    def _get_email_field(self):
        return self.wait_for_element_visibility_located_by(locator = self.EMAIL_INPUT)

    def _get_password_input (self):
        return self.wait_for_element_visibility_located_by(locator = self.PASSWORD_INPUT)

    def _get_submit_button(self):
        return self.wait_for_element_visibility_located_by(locator = self.SUBMIT_BUTTON)

    def click_sign_in_button(self):
        self._get_sign_in_button().click()

    def enter_email (self, email):
        self._get_email_field().send_keys(email)

    def enter_password (self, password):
        self._get_password_input().send_keys(password)

    def submit_credentials (self):
        self._get_submit_button().click()
        return UserPersonalPage(driver = self.driver)



