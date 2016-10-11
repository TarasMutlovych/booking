from .base_page import BasePage
from selenium.webdriver.common.by import By


class UserPersonalPage(BasePage):

    USER_FIRST_NAME = (By.CSS_SELECTOR, "span.header_name.user_firstname")
    USER_LAST_NAME = (By.CSS_SELECTOR, "span.header_name.user_lastname")

    def _get_first_name_webelement(self):
        return self.wait_for_element_visibility_located_by(locator = self.USER_FIRST_NAME)

    def _get_last_name_webelement(self):
        return self.wait_for_element_visibility_located_by(locator = self.USER_LAST_NAME)

    def get_first_name(self):
        return self._get_first_name_webelement().text

    def get_last_name(self):
        return self._get_last_name_webelement().text
