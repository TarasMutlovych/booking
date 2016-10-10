from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.webdriver_provider import WebDriverProvider

class BasePage(object):

    def __init__(self, driver = None, URL_booking = "http://www.booking.com/"):
        self.driver = driver if driver else WebDriverProvider.get_chrome_driver(URL = URL_booking)

    def wait_for_element_visibility_located_by (self, locator):
        return WebDriverWait(driver =self.driver, timeout=15).\
            until(EC.visibility_of_element_located(locator = locator))

    def wait_for_element_to_be_clickable_located(self, locator):
        return WebDriverWait(driver = self.driver, timeout=15).\
            until(EC.element_to_be_clickable(locator = locator))