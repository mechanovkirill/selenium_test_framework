from selenium import webdriver
from framework.browsers.browser_factory import BrowserFactory
import logging

logger = logging.getLogger(__name__)


class Browser:
    driver: webdriver = None

    @classmethod
    def get_driver(cls) -> webdriver:
        if cls.driver is not None:
            return cls.driver
        else:
            cls.driver = BrowserFactory().get_chosen_driver()
            return cls.driver

    def quit(self) -> None:
        self.get_driver().quit()
        Browser.driver = None

    def go_to_url(self, url) -> None:
        self.get_driver().get(url)

    def take_screenshot(self, filename):
        self.get_driver().save_screenshot(filename)
