from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By
from  .user_personal_page import UserPersonalPage


class StartPage(BasePage):

    SIGN_IN_BUTTON = (By.XPATH, ".//li[@id = 'current_account'][position() = 2]//div")
    EMAIL_INPUT = (By.CLASS_NAME, "user_access_email")
    PASSWORD_INPUT = (By.CLASS_NAME, "user_access_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "div.form-shown-section form.user_access_form-user_avatar--circle input[type = 'submit']")

    SEARCH_FORM = (By.CSS_SELECTOR, "form[id='frm'][data-is-first-visible = '1']")
    BOOKING_LOGO = (By.CSS_SELECTOR, "img#logo_no_globe_new_logo")
    SEARCH_INPUT = (By.ID, "ss")
    # SEARCH_HOTEL_AUTOCOMPILE = (By.ID, "ul.c-autocomplete__list.sb-autocomplete__list.-visible")
    FIRST_OPTION_IN_AUTOCOMPILE = (By.XPATH, ".//ul[@class = 'c-autocomplete__list sb-autocomplete__list -visible']/li[position() = 1]")

    def _get_sign_in_button (self):
        return self.wait_for_element_visibility_located_by(locator= self.SIGN_IN_BUTTON)

    def _get_email_field(self):
        return self.wait_for_element_visibility_located_by(locator = self.EMAIL_INPUT)

    def _get_password_input (self):
        return self.wait_for_element_visibility_located_by(locator = self.PASSWORD_INPUT)

    def _get_submit_button(self):
        return self.wait_for_element_visibility_located_by(locator = self.SUBMIT_BUTTON)

    def _get_search_form(self):
       return self.wait_for_element_visibility_located_by(locator = self.SEARCH_FORM)

    def _get_booking_logo(self):
        return self.wait_for_element_visibility_located_by(locator = self.BOOKING_LOGO)

    def _get_search_input(self):
        return self.wait_for_element_visibility_located_by(locator = self.SEARCH_INPUT)

    # def _get_search_autocompile_list(self):
    #     return self.wait_for_element_visibility_located_by(locator = self.SEARCH_HOTEL_AUTOCOMPILE)

    def _get_first_autocompile_option(self):
        return self.wait_for_element_visibility_located_by(locator = self.FIRST_OPTION_IN_AUTOCOMPILE)

    def click_sign_in_button(self):
        self._get_sign_in_button().click()

    def enter_email (self, email):
        self._get_email_field().send_keys(email)

    def enter_password (self, password):
        self._get_password_input().send_keys(password)

    def submit_credentials (self):
        self._get_submit_button().click()
        return UserPersonalPage(driver = self.driver)

    def make_sure_start_page_is_opened(self):
        try:
            self._get_search_form().click()
        except TimeoutException:
            self._get_booking_logo().click()

    def enter_hotel(self, hotel):
        self._get_search_input().send_keys(hotel)

    def select_first_item_from_autocompile(self):
        #self._get_search_autocompile_list()
        self._get_first_autocompile_option().click()







