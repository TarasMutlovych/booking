from unittest import TestCase
from source_code.start_page import StartPage
from source_code.user_personal_page import UserPersonalPage

class Test(TestCase):

    USER_EMAIL = "patriotl@i.ua"
    USER_PASS = "dominic0018"

    FIRTS_NAME = "Taras1"
    LAST_NAME = "Mytlovych1"

    def test_a_user_name(self):
        start_page = StartPage()
        start_page.click_sign_in_button()
        start_page.enter_email(self.USER_EMAIL)
        start_page.enter_password(self.USER_PASS)
        user_personal_page = start_page.submit_credentials()

        self.assertEqual(self.FIRTS_NAME + ' ' + self.LAST_NAME,
                         user_personal_page.get_first_name() + ' ' + user_personal_page.get_last_name(),
                         "User name and surname is not as expected. Searched for %s %s but found %s %s" %
                         (self.FIRTS_NAME, self.LAST_NAME,
                          user_personal_page.get_first_name(), user_personal_page.get_last_name()))

    



