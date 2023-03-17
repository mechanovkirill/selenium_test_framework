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

    def get_chosen_driver(self) -> webdriver:
        try:
            if self.browser_type.lower() == "chrome":
                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            if self.browser_type.lower() == "firefox":
                return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            else:
                logger.error(f"Driver not found for browser {self.browser_type}. Check config.json.")
        except WebDriverException:
            logger.error(f"Getting driver error {traceback.format_exc()}")
