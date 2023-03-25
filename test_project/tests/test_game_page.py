import pytest
from framework.utils.data_manager import DataManager
from test_project.pages.main_page import MainPage
from test_project.pages.game_page_card_1 import GamePageCardOne
from test_project.pages.game_page_card_2 import GamePageCardTwo


class TestGamePage:
    def test_help_form(self):
        main_page = MainPage()
        game_page_card_1 = GamePageCardOne()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page_card_1.is_open() is True, "Game page is not open."
        game_page_card_1.click_to_help_button()
        assert game_page_card_1.is_help_response_displayed() is True, 'Help response is not displayed.'

    def test_timer_correct_starts(self):
        main_page = MainPage()
        game_page_card_1 = GamePageCardOne()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page_card_1.is_open() is True, "Game page is not open."
        timer_value = game_page_card_1.get_timer_value()
        assert timer_value == '00:00:00', "Timer starts not from zero."

    def test_valid_password(self):
        main_page = MainPage()
        game_page_card_1 = GamePageCardOne()
        game_page_card_2 = GamePageCardTwo()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page_card_1.is_open() is True, "Game page is not open."
        game_page_card_1.input_random_valid_email()
        game_page_card_1.input_random_valid_password()
        game_page_card_1.accept_terms_and_conditions()
        game_page_card_1.click_to_the_next_button()
        assert game_page_card_2.is_open() is True, "Card 2 is not opened."

    @pytest.mark.parametrize(
        "password",
        DataManager().get_game_page_test_data().invalid_passwords,
        ids=["void password", "just spaces", "short", "without digits",
             "without upper", "without cyrillic", "without email characters"]
    )
    def test_invalid_password(self, password):
        main_page = MainPage()
        game_page_card_1 = GamePageCardOne()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page_card_1.is_open() is True, "Game page is not open."
        game_page_card_1.input_random_valid_email()
        game_page_card_1.input_random_invalid_password(password=password)
        game_page_card_1.accept_terms_and_conditions()
        game_page_card_1.click_to_the_next_button()
        assert game_page_card_1.is_open() is True, "Card 2 is opened."

    @pytest.mark.parametrize('domain', ['other', '.jpg'])
    def test_invalid_top_level_domain(self, domain):
        main_page = MainPage()
        game_page_card_1 = GamePageCardOne()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page_card_1.is_open() is True, "Game page is not open."
        game_page_card_1.input_invalid_email(domain)
        game_page_card_1.input_random_valid_password()
        game_page_card_1.accept_terms_and_conditions()
        game_page_card_1.click_to_the_next_button()
        assert game_page_card_1.is_open() is True, "Card 2 is opened."

    def test_valid_image_upload(self):
        main_page = MainPage()
        game_page_card_1 = GamePageCardOne()
        game_page_card_2 = GamePageCardTwo()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page_card_1.is_open() is True, "Game page is not open."
        game_page_card_1.input_random_valid_email()
        game_page_card_1.input_random_valid_password()
        game_page_card_1.accept_terms_and_conditions()
        game_page_card_1.click_to_the_next_button()
        assert game_page_card_2.is_open() is True, "Card 2 is not opened."
        game_page_card_2.upload_valid_image()
        game_page_card_2.select_3_checkboxes()
        game_page_card_2.click_to_the_card_2_next_button()
        assert game_page_card_2.card_3_is_open() is True, "Card 3 is not opened."
