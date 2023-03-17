from selenium import webdriver
from framework.browsers.browser_factory import BrowserFactory
import logging

from framework.utils.data_manager import ConfigData

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
                f"Launch [{cls.config.browser}] browser with options {cls.config.browsers_options} "
                f"{cls.config.chrome_options if cls.config.browser == 'Chrome' else cls.config.firefox_options}."
            )
            return cls.driver

    def quit(self) -> None:
        self.get_driver().quit()
        Browser.driver = None
        logger.info(f"Browser quit.")

    def go_to_url(self, url) -> None:
        self.get_driver().get(url)

    def take_screenshot(self, filename):  # TODO typing
        self.get_driver().save_screenshot(filename)
