from selenium.webdriver.common.by import By
from framework.browsers.browser import Browser
from framework.conditional_waits import Waits


class BaseForm:
    def __init__(self, unique_locator: tuple[By, str], name: str) -> None:
        self.name = name
        self.unique_locator = unique_locator
        self.browser = Browser()
        self.driver = self.browser.get_driver()
        self.wait_for = Waits(driver_=self.driver, config_=self.browser.config)

    def is_open(self) -> bool:
        return self.wait_for.visibility_of_element_located(self.unique_locator, self.name).is_displayed()
