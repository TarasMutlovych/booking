from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .destination_search_result import DestinationSearchResult
from selenium import webdriver
import time


class DestinationTips(BasePage):

    DESTINATION_INPUT_FIELD = (By.CSS_SELECTOR, "input.js-autocomplete-locations.dsf_search_input")
    SUGGESTION_HEADERS = (By.CSS_SELECTOR, "div.ac_elements__suggestion span.result_text_left b.search_hl_name")
    AUTOCOMPILE_LIST = (By.CSS_SELECTOR, "div[data-component-request-type = 'location']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "i.bicon.bicon-search")


    def _get_destination_input_field(self):
        return self.wait_for_element_visibility_located_by(locator = self.DESTINATION_INPUT_FIELD)

    def _get_suggestion_headers(self, header):
        #time.sleep(3)
        self.wait_for_element_visibility_located_by(self.AUTOCOMPILE_LIST)
        SUGGESTION_HEADERS1 = self.wait_for_visibility_of_any_element(self.SUGGESTION_HEADERS)
        for element in SUGGESTION_HEADERS1:
            if element.text == header:
                return element

    def _get_search_button(self):
        return self.wait_for_element_visibility_located_by(locator = self.SEARCH_BUTTON)

    def enter_location_into_search_field(self, location):
        self._get_destination_input_field().send_keys(location)

    def select_suggestion(self, suggestion):
        try:
            self._get_suggestion_headers(header = suggestion).click()
        except AttributeError:
            print "%s is not found in suggestion list" % (suggestion)

    def click_search_button(self):
        self._get_search_button().click()
        # self.mouse = webdriver.ActionChains(self.driver)
        # self.mouse.move_to_element(self._get_search_button()).click().perform()
        #self.driver.execute_script("arguments[0].click();", self._get_search_button())
        return DestinationSearchResult(driver = self.driver)

