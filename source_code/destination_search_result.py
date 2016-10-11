from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By


class DestinationSearchResult(BasePage):

    REGION_DESTINATION_TITLE = (By.CSS_SELECTOR, "div.dsf-interests-title")
    CITY_DESTINATION_TITLE = (By.CSS_SELECTOR, "h1.header_full_image__main_title")

    def _get_destination_result_title(self):
        try:
            return self.wait_for_element_visibility_located_by(locator = self.REGION_DESTINATION_TITLE)
        except TimeoutException:
            return self.wait_for_element_visibility_located_by(locator=self.CITY_DESTINATION_TITLE)

    def get_title_text(self):
        return self._get_destination_result_title().text

