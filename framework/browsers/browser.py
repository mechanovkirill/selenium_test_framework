import typing

from selenium.webdriver.remote import webdriver
from framework.browsers.browser_factory import BrowserFactory
from framework.browsers.js_scripts import JSActions
from framework.utils.data_manager import ConfigData
import logging

logger = logging.getLogger(__name__)


class Browser:
    driver: webdriver = None
    config: ConfigData = None

    @classmethod
    def get_driver(cls) -> webdriver:
        if cls.driver is not None:
            return cls.driver
        else:
            factory_data: tuple = BrowserFactory().get_chosen_driver_and_config()
            cls.driver = factory_data[0]
            cls.config = factory_data[1]
            logger.info(
                f"| Launch [{cls.config.browser}] browser with options {cls.config.browsers_options} "
                f"{cls.config.chrome_options if cls.config.browser.lower() == 'chrome' else cls.config.firefox_options}."
            )
            return cls.driver

    def quit(self) -> None:
        self.get_driver().quit()
        Browser.driver = None
        logger.info(f"| Browser quit.")

    def go_to_url(self, url) -> None:
        self.get_driver().get(url)

    def js_scroll_into_view(self, element) -> None:
        JSActions(self.get_driver()).scroll_into_view(element)

    def take_screenshot(self, path_file: str) -> None:
        self.get_driver().save_screenshot(path_file)

