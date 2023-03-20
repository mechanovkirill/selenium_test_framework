from framework.base_form import BaseForm
from selenium.webdriver.common.by import By
from framework.elements.elements import Button, Div, Input
from framework.utils.data_manager import DataManager


class GamePage(BaseForm):
    HELP_BUTTON_LOCATOR = (By.XPATH, "//a[@class='help-form__help-button' and text()='Help']")
    HELP_RESPONSE_LOCATOR = (By.XPATH, "//div[@class='help-form__response' and contains(text(), 'Please wait')]")
    TIMER_LOCATOR = (By.XPATH, "//div[contains(@class, 'timer')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Password')]")
    EMAIL_INPUT = (By.XPATH, "//input[contains(@placeholder, 'email')]")
    DOMAIN_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Domain')]")
    DOMAIN_ZONE = (By.XPATH, "//div[@class='dropdown__list']//div[text()='.org']")
    ACCEPT_CHECK = (By.XPATH, '')

    def __init__(self) -> None:
        super().__init__(
            unique_locator=(By.XPATH, "//input[contains(@placeholder, 'Password')]"),
            name='Game_Page'
        )
        self.test_data = DataManager().get_game_page_test_data()
        # elements:
        self.help_response_div = Div(self.HELP_RESPONSE_LOCATOR, 'Div Help Response')
        self.help_button = Button(self.HELP_BUTTON_LOCATOR, 'Help Button')
        self.timer_div = Div(self.TIMER_LOCATOR, 'Div Timer')
        self.email_input = Input(self.EMAIL_INPUT, 'Email input')
        self.email_domain_input = Input(self.DOMAIN_INPUT, 'Email domain input')
        self.password_input = Input(self.PASSWORD_INPUT, 'Password input')
        self.domain_zone = Div(self.DOMAIN_ZONE, 'Domain zone select')

    def click_to_help_button(self) -> None:
        self.help_button.click()

    def is_help_response_displayed(self) -> bool:
        return self.help_response_div.is_displayed()

    def get_timer_value(self) -> str:
        return self.timer_div.get_text()

    def input_random_valid_email(self) -> None:
        self.email_input.clear()
        self.email_input.fill_the_field(self.test_data.valid_rand_email_name)
        self.email_domain_input.clear()
        self.email_domain_input.fill_the_field(self.test_data.valid_rand_email_domain)
        self.domain_zone.click()

    def input_random_valid_password(self) -> None:
        pass
