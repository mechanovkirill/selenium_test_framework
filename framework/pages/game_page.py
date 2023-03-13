from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.common.by import By
from framework.utils.config_data import ConfigData

config = ConfigData()


class GamePage:
    def __init__(self, driver: webdriver.Chrome, config_: ConfigData() = config) -> None:
        self.driver = driver
        self.url = config_.host_url
        self.timeout = config.time

    HERE_LINK_LOCATOR = (By.XPATH, "//a[@class='start__link' and (@href='/game.html' or contains(text(), 'HERE'))]")
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Password')]")
    HELP_BUTTON_LOCATOR = (By.XPATH, "//a[@class='help-form__help-button' and text()='Help']")
    HELP_RESPONSE_LOCATOR = (By.XPATH, "//div[@class='help-form__response' and contains(text(), 'Please wait')]")
    TIMER_LOCATOR = (By.XPATH, "//div[contains(@class, 'timer')]")

    def navigate_to_main_page(self) -> None:
        self.driver.get(self.url)

    def is_main_page_opened(self) -> bool:
        is_opened = WDWait(self.driver, self.timeout).until(
            exp_cond.visibility_of_element_located(self.HERE_LINK_LOCATOR)
        ).is_displayed()
        return is_opened

    def click_to_here_link(self) -> None:
        self.driver.find_element(*self.HERE_LINK_LOCATOR).click()

    def is_game_page_opened(self) -> bool:
        is_opened = WDWait(self.driver, self.timeout).until(
            exp_cond.visibility_of_element_located(self.PASSWORD_INPUT_LOCATOR)
        ).is_displayed()
        return is_opened

    def click_to_help_button(self) -> None:
        WDWait(self.driver, self.timeout).until(
            exp_cond.visibility_of_element_located(self.HELP_BUTTON_LOCATOR)
        ).click()

    def is_help_response_displayed(self) -> bool:
        is_opened = WDWait(self.driver, self.timeout).until(
            exp_cond.visibility_of_element_located(self.HELP_RESPONSE_LOCATOR)
        ).is_displayed()
        return is_opened

    def get_timer_value(self) -> str:
        timer_value = WDWait(self.driver, self.timeout).until(
            exp_cond.presence_of_element_located(self.TIMER_LOCATOR)
        ).text
        return timer_value
