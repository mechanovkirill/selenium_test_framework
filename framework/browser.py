import traceback
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from framework.utils.data_manager import ConfigData
import logging

logger = logging.getLogger(__name__)

config = ConfigData()


class BrowserFactory:
    def __init__(self, config_=config):
        self.browser_type = config_.browser

    def get_driver_options(self):
        pass

    def get_driver(self) -> webdriver:
        try:
            if self.browser_type.lower() == "chrome":
                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            if self.browser_type.lower() == "firefox":
                return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            else:
                logger.error(f"Driver not found for browser {self.browser_type}.")
        except WebDriverException:
            logger.error(f"Getting driver error {traceback.format_exc()}")


class Browser:
    driver = None
    #
    # def __init__(self, optional_driver):
    #     if Browser.driver is None:
    #         Browser.driver = optional_driver
    #
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return cls.driver

    def go_to_url(self, url) -> None:
        self.get_driver().get(url)

    def quit(self) -> None:
        self.get_driver().quit()
        Browser.driver = None

    def take_screenshot(self, filename):
        self.get_driver().save_screenshot(filename)
