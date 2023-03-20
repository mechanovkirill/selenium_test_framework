from test_project.pages.main_page import MainPage
from test_project.pages.game_page import GamePage

import time


class TestGamePage:
    def test_help_form(self):
        main_page = MainPage()
        game_page = GamePage()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page.is_open() is True, "Game page is not open."
        game_page.click_to_help_button()
        assert game_page.is_help_response_displayed() is True, 'Help response is not displayed.'

    def test_timer_correct_starts(self):
        main_page = MainPage()
        game_page = GamePage()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page.is_open() is True, "Game page is not open."
        timer_value = game_page.get_timer_value()
        assert timer_value == '00:00:00', "Timer starts not from zero."

    def test_valid_password(self):
        main_page = MainPage()
        game_page = GamePage()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page.is_open() is True, "Game page is not open."
        game_page.input_random_valid_email()
        game_page.input_random_valid_password()
        game_page.accept_terms_and_conditions()
        game_page.click_to_the_next_button()
        assert game_page.card_2_is_open() is True, "Card 2 is not opened."

    def test_invalid_password(self):
        main_page = MainPage()
        game_page = GamePage()

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened."
        main_page.click_to_here_link()
        assert game_page.is_open() is True, "Game page is not open."
        game_page.input_random_valid_email()
        game_page.input_random_valid_password()
        game_page.accept_terms_and_conditions()
        game_page.click_to_the_next_button()
        # assert game_page.card_2_is_open() is False, "Card 2 is opened."