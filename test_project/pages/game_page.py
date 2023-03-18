from framework.base_form import BaseForm
from selenium.webdriver.common.by import By
from framework.elements.elements import Button, Div


class GamePage(BaseForm):
    HELP_BUTTON_LOCATOR = (By.XPATH, "//a[@class='help-form__help-button' and text()='Help']")
    HELP_RESPONSE_LOCATOR = (By.XPATH, "//div[@class='help-form__response' and contains(text(), 'Please wait')]")
    TIMER_LOCATOR = (By.XPATH, "//div[contains(@class, 'timer')]")

    def __init__(self) -> None:
        super().__init__(
            unique_locator=(By.XPATH, "//input[contains(@placeholder, 'Password')]"),
            name='Game_Page'
        )
        # elements:
        self.help_response_div = Div(self.HELP_RESPONSE_LOCATOR, 'Div Help Response')
        self.help_button = Button(self.HELP_BUTTON_LOCATOR, 'Help Button')
        self.timer_div = Div(self.TIMER_LOCATOR, 'Div Timer')

    def click_to_help_button(self) -> None:
        self.help_button.click()

    def is_help_response_displayed(self) -> bool:
        return self.help_response_div.is_displayed()

    def get_timer_value(self) -> str:
        return self.timer_div.get_text()
