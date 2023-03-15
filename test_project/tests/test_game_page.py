from test_project.pages.main_page import MainPage
from test_project.pages.game_page import GamePage


class TestGamePage:
    def test_help_form(self, driver):
        main_page = MainPage(driver)
        game_page = GamePage(driver)

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened"
        main_page.click_to_here_link()
        assert game_page.is_open() is True, "Game page is not open"
        game_page.click_to_help_button()
        assert game_page.is_help_response_displayed() is True, 'Help response is not displayed'

    def test_timer_correct_starts(self, driver):
        main_page = MainPage(driver)
        game_page = GamePage(driver)

        main_page.open()
        assert main_page.is_open() is True, "Main page is not opened"
        main_page.click_to_here_link()
        assert game_page.is_open() is True, "Game page is not open"
        timer_value = game_page.get_timer_value()
        assert timer_value == '00:00:00', "Timer starts not from zero"
