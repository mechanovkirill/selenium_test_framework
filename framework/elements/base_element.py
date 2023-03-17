import traceback
from selenium.common import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.common.by import By
from framework.logging import LOGGING_CONFIG
import logging.config
from framework.browsers.browser import Browser

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class BaseElement:
    def __init__(self, locator: tuple[By, str], name: str):
        self.locator = locator
        self.name = name
        self.browser = Browser()
        self.driver = self.browser.get_driver()

    def _find_element(self) -> WebElement:
        try:
            logger.info(f"finding element {self.name}")
            return WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator))
        except WebDriverException:
            logger.warning(f"_find_element {self.name} failed  {traceback.format_exc()}")

    def click(self) -> None:
        try:
            if WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator)).is_enabled():
                WDWait(self.driver, 10).until(exp_cond.element_to_be_clickable(self.locator)).click()
                logger.info(f"Click to {self.name}")
            else:
                logger.info(f"{self.name} element is not enabled")
        except WebDriverException:
            logger.warning(f"BaseElement click failed {self.name} {traceback.format_exc()}")

    def is_displayed(self) -> bool:
        try:
            logger.info(f"is_displayed applied to {self.name}")
            return WDWait(self.driver, 10).until(exp_cond.visibility_of_element_located(self.locator)).is_displayed()
        except WebDriverException:
            logger.warning(f"is_displayed {self.name} failed {traceback.format_exc()}")

    def get_text(self) -> str:
        try:
            logger.info(f"get_text applied to {self.name}")
            return self._find_element().text
        except WebDriverException:
            logger.warning(f"get_text {self.name} failed {traceback.format_exc()}")
