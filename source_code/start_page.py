from selenium import webdriver
from .base_page import BasePage
from selenium.webdriver.common.by import By



class StartPage(BasePage):

    SIGN_IN_BUTTON = (By.XPATH, "from selenium.webdriver.common.by import By")

    def _get_sign_in_button (self):
        return self.wait_for_element_visibility_located_by(locator= self.SIGN_IN_BUTTON)

    def click_sign_in_button(self):
        self._get_sign_in_button().click()

