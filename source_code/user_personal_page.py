from .base_page import BasePage
from selenium.webdriver.common.by import By
from .destination_tips import DestinationTips


class UserPersonalPage(BasePage):

    USER_FIRST_NAME = (By.CSS_SELECTOR, "span.header_name.user_firstname")
    USER_LAST_NAME = (By.CSS_SELECTOR, "span.header_name.user_lastname")

    DESTINATION_TIP_BUTTON = (By.XPATH, "//a[@class = 'header_link_new_icon popover_trigger']")
    LETS_GO_BUTON = (By.CSS_SELECTOR, "dd.dsf_banner_awareness_index_cta")

    def _get_first_name_webelement(self):
        return self.wait_for_element_visibility_located_by(locator = self.USER_FIRST_NAME)

    def _get_last_name_webelement(self):
        return self.wait_for_element_visibility_located_by(locator = self.USER_LAST_NAME)

    def _get_destination_tips(self):
        return self.wait_for_element_visibility_located_by(locator = self.DESTINATION_TIP_BUTTON)

    def _get_lets_go_button(self):
        return self.wait_for_element_visibility_located_by(locator = self.LETS_GO_BUTON)

    def get_first_name(self):
        return self._get_first_name_webelement().text

    def get_last_name(self):
        return self._get_last_name_webelement().text

    def click_destination_tips_button(self):
        self._get_destination_tips().click()

    def click_lets_go_button(self):
        self._get_lets_go_button().click()
        return DestinationTips(driver = self.driver)


