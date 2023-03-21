from framework.base_form import BaseForm
from selenium.webdriver.common.by import By
from framework.elements.elements import Button, Div, Input, Span, Link
from framework.utils.data_manager import DataManager


class GamePage(BaseForm):
    HELP_BUTTON_LOCATOR = (By.XPATH, "//a[@class='help-form__help-button' and text()='Help']")
    HELP_RESPONSE_LOCATOR = (By.XPATH, "//div[@class='help-form__response' and contains(text(), 'Please wait')]")
    TIMER_LOCATOR = (By.XPATH, "//div[contains(@class, 'timer')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Password')]")
    EMAIL_INPUT = (By.XPATH, "//input[contains(@placeholder, 'email')]")
    DOMAIN_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Domain')]")
    DROPDOWN_OTHER = (By.XPATH, "//div[@class='dropdown__field' and text()='other']")
    DOMAIN_ZONE_DOT_ORG = (By.XPATH, "//div[@class='dropdown__list']//div[text()='.org']")
    ACCEPT_TERMS_CHECKBOX = (By.XPATH, "//span[contains(@class, 'checkbox__check')]")
    NEXT_LINK = (By.XPATH, "//a[text()='Next']")
    CARD_2_DOWNLOAD_BUTTON = (By.XPATH, "//button[@name='button' and text()='Download image']")

    def __init__(self) -> None:
        super().__init__(
            unique_locator=(By.XPATH, "//input[contains(@placeholder, 'Password')]"),
            name='Game Page(card 1)'
        )
        self.test_data = DataManager().get_game_page_test_data()
        # elements:
        self.help_response_div = Div(self.HELP_RESPONSE_LOCATOR, 'Div Help Response')
        self.help_button = Button(self.HELP_BUTTON_LOCATOR, 'Help Button')
        self.timer_div = Div(self.TIMER_LOCATOR, 'Div Timer')
        self.email_input = Input(self.EMAIL_INPUT, 'Email input')
        self.email_domain_input = Input(self.DOMAIN_INPUT, 'Email domain input')
        self.password_input = Input(self.PASSWORD_INPUT, 'Password input')
        self.dropdown_field = Div(self.DROPDOWN_OTHER, 'Dropdown select menu')
        self.domain_zone_dot_org = Div(self.DOMAIN_ZONE_DOT_ORG, 'Domain zone select')
        self.accept_terms_checkbox = Span(self.ACCEPT_TERMS_CHECKBOX, 'Accept terms checkbox')
        self.next_link = Link(self.NEXT_LINK, 'Next link')
        self.card_2_download_button = Button(self.CARD_2_DOWNLOAD_BUTTON, 'Download button')

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
        self.dropdown_field.click()
        self.domain_zone_dot_org.click()

    def input_random_valid_password(self) -> None:
        self.password_input.clear()
        self.password_input.fill_the_field(self.test_data.valid_rand_password)

    def accept_terms_and_conditions(self) -> None:
        self.browser.js_scroll_into_view(self.accept_terms_checkbox)
        self.accept_terms_checkbox.click()

    def click_to_the_next_button(self) -> None:
        self.next_link.click()

    def card_2_is_open(self) -> bool:
        return self.card_2_download_button.is_displayed()

    def input_random_invalid_password(self, password) -> None:
        self.password_input.clear()
        self.password_input.fill_the_field(password)
