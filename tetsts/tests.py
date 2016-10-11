from unittest import TestCase
from source_code.start_page import StartPage
from source_code.user_personal_page import UserPersonalPage
from source_code.destination_tips import DestinationTips
from source_code.destination_search_result import DestinationSearchResult

class Test(TestCase):

    USER_EMAIL = "patriotl@i.ua"
    USER_PASS = "dominic0018"

    FIRTS_NAME = "Taras"
    LAST_NAME = "Mytlovych"

    LOCATION = "Lviv"
    DESTINATION_SUGGESTIONS = "Lviv Region"

    # def test_a_user_name(self):
    #     start_page = StartPage()
    #     start_page.click_sign_in_button()
    #     start_page.enter_email(self.USER_EMAIL)
    #     start_page.enter_password(self.USER_PASS)
    #     user_personal_page = start_page.submit_credentials()
    #
    #     self.assertEqual(self.FIRTS_NAME + ' ' + self.LAST_NAME,
    #                      user_personal_page.get_first_name() + ' ' + user_personal_page.get_last_name(),
    #                      "User name and surname is not as expected. Searched for %s %s but found %s %s" %
    #                      (self.FIRTS_NAME, self.LAST_NAME,
    #                       user_personal_page.get_first_name(), user_personal_page.get_last_name()))
    #
    # def test_b_destibaion_tips(self):
    #     user_personal_page = UserPersonalPage()
    #     user_personal_page.click_destination_tips_button()
    #     destination_tips = user_personal_page.click_lets_go_button()
    #     destination_tips.enter_location_into_search_field(location = self.LOCATION)
    #     destination_tips.select_suggestion(self.DESTINATION_SUGGESTIONS)
    #     destination_search_results = destination_tips.click_search_button()
    #
    #     self.assertTrue(self.DESTINATION_SUGGESTIONS in destination_search_results.get_title_text(),
    #                     "Destination is not found. You were loking for %s, but found %s" % (
    #                         self.DESTINATION_SUGGESTIONS, destination_search_results.get_title_text()
    #                     ))

    def test_c_Montenegro_hotel(self):
        start_page = StartPage()
        start_page.make_sure_start_page_is_opened()
        start_page.enter_hotel("Montenegro Rio")
        start_page.select_first_item_from_autocompile()











