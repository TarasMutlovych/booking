from os import *
from selenium import webdriver


class WebDriver:

    @classmethod
    def set_chrome_driver(cls):
        usr_path = path.expanduser("~")
        chrome_driver_path = path.join(usr_path, "PycharmProjects", "insurance", "library", "chromedriver.exe")
        cls.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    @classmethod
    def get_chrome_driver(cls, URL):
        if cls.driver is None:
            cls.set_chrome_driver()
            cls.driver.maximize_window()
            cls.driver.get(URL)
        return cls.driver

