import traceback
from selenium.common import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from framework.logging import LOGGING_CONFIG
from framework.browsers.browser import Browser
from framework.conditional_waits import Waits
import logging.config

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class BaseElement:
    def __init__(self, locator: tuple[By, str], name: str):
        self.locator: tuple[By, str] = locator
        self.name: str = name
        self.browser = Browser()
        self.driver = self.browser.get_driver()
        self.wait_for = Waits(driver_=self.driver, config_=self.browser.config)

    def _find_element(self) -> WebElement:
        try:
            logger.info(f"| Finding an element {self.name}")
            return self.wait_for.element_to_be_present(self.locator, self.name)
        except WebDriverException:
            logger.warning(f"| Method _find_element {self.name} failed  {traceback.format_exc()}")

    def click(self) -> None:
        try:
            if self._find_element().is_enabled():
                self.wait_for.element_to_be_clickable(self.locator, self.name).click()
                logger.info(f"| Click to {self.name}")
            else:
                logger.warning(f"| {self.name} element is not enabled")
        except WebDriverException:
            logger.warning(f"| BaseElement click failed {self.name} {traceback.format_exc()}")

    def is_displayed(self) -> bool:
        try:
            logger.info(f"| Method is_displayed applied to {self.name}")
            return self.wait_for.visibility_of_element_located(self.locator, self.name).is_displayed()
        except WebDriverException:
            logger.warning(f"| Method is_displayed {self.name} failed {traceback.format_exc()}")

    def get_text(self) -> str:
        try:
            logger.info(f"| Method get_text applied to {self.name}")
            return self._find_element().text
        except WebDriverException:
            logger.warning(f"| Method get_text {self.name} failed {traceback.format_exc()}")
