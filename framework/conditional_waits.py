from typing import Iterable, Type
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium import webdriver
from framework.utils.data_manager import ConfigData
import logging

logger = logging.getLogger(__name__)


class Waits:
    def __init__(self, driver_: webdriver, config_: ConfigData()):
        self.driver = driver_
        self.timeout: float = config_.timeout
        self.polling_interval: float = config_.poll_frequency

    def web_driver_wait(
            self,
            condition_name: str,
            ignored_exceptions: Iterable[Type[Exception]] = None,
    ) -> WebDriverWait:
        """condition_name- is just for logging!!!"""
        logger.info(f"| Wait for {condition_name}")

        return WebDriverWait(self.driver, self.timeout, self.polling_interval, ignored_exceptions=ignored_exceptions)

    def element_to_be_present(self, locator: tuple[By, str]) -> webelement:
        return self.web_driver_wait("element_to_be_present").until(
            expected_conditions.presence_of_element_located(locator)
        )

    def element_to_be_clickable(self, locator: tuple[By, str]) -> webelement:
        return self.web_driver_wait("element_to_be_clickable").until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def visibility_of_element_located(self, locator: tuple[By, str]) -> webelement:
        return self.web_driver_wait("visibility_of_element_located").until(
            (expected_conditions.visibility_of_element_located(locator))
        )
