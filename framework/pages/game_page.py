from framework.pages.base_form import BaseForm
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.common.by import By
from framework.utils.config_data import ConfigData

config = ConfigData()


class GamePage(BaseForm):
    def __init__(self, driver) -> None:
        super().__init__(
            name='game_page',
            unique_locator=(By.XPATH, "//input[contains(@placeholder, 'Password')]")
        )
        self.driver = driver

    HELP_BUTTON_LOCATOR = (By.XPATH, "//a[@class='help-form__help-button' and text()='Help']")
    HELP_RESPONSE_LOCATOR = (By.XPATH, "//div[@class='help-form__response' and contains(text(), 'Please wait')]")
    TIMER_LOCATOR = (By.XPATH, "//div[contains(@class, 'timer')]")

    def click_to_help_button(self) -> None:  # TODO: timeout
        WDWait(self.driver, 10).until(
            exp_cond.visibility_of_element_located(self.HELP_BUTTON_LOCATOR)
        ).click()

    def is_help_response_displayed(self) -> bool:
        is_opened = WDWait(self.driver, 10).until(
            exp_cond.visibility_of_element_located(self.HELP_RESPONSE_LOCATOR)
        ).is_displayed()
        return is_opened

    def get_timer_value(self) -> str:
        timer_value = WDWait(self.driver, 10).until(
            exp_cond.presence_of_element_located(self.TIMER_LOCATOR)
        ).text
        return timer_value
