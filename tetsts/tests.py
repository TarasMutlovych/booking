from unittest import TestCase
from source_code.start_page import StartPage


class Test(TestCase):
    LOGIN = "patriotl@i.ua"
    PASS = "dominic0018"
    FIRTS_NAME = "Taras"
    LAST_NAME = "Mytlovych"

    def test_user_name(self):
        start_page = StartPage()
        start_page.click_sign_in_button()
