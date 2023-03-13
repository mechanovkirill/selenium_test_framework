from framework.pages.game_page import GamePage


class TestHelpForm:

    def test_help_form(self, driver):
        game_page = GamePage(driver)

        game_page.navigate_to_main_page()
        is_main_page_opened = game_page.is_main_page_opened()
        assert is_main_page_opened is True, "Main page is not open"

        game_page.click_to_here_link()
        is_game_page_opened = game_page.is_game_page_opened()
        assert is_game_page_opened is True, "Game page is not open"

        game_page.click_to_help_button()
        is_help_response_displayed = game_page.is_help_response_displayed()
        assert is_help_response_displayed is True, 'Help response is not displayed'

    def test_timer_correct_starts(self, driver):
        game_page = GamePage(driver)

        game_page.navigate_to_main_page()
        is_main_page_opened = game_page.is_main_page_opened()
        assert is_main_page_opened is True, "Main page is not open"

        game_page.click_to_here_link()
        timer_value = game_page.get_timer_value()
        is_game_page_opened = game_page.is_game_page_opened()
        assert is_game_page_opened is True, "Game page is not open"
        assert timer_value == '00:00:00', "Timer starts not from zero"
