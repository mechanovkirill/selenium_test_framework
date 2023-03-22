import traceback
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFox_options
from framework.utils.data_manager import DataManager, ConfigData
import logging

logger = logging.getLogger(__name__)


class BrowserFactory:
    """Receives are options from config.json file and return tuple contained driver instance according to configuration
    and dataclass with configuration.
    Supported browsers are Chrome, Firefox. How to with config file described in the README."""

    def __init__(self, config_=DataManager()):
        self.config: ConfigData = config_.get_config_data()
        self.browser_type: str = self.config.browser
        self.browsers_options: tuple[dict] = self.config.browsers_options
        self.chrome_options: tuple[str] = self.config.chrome_options
        self.firefox_options: tuple[str] = self.config.firefox_options

    def _get_browser_options(self) -> Options:
        try:
            options = None

            if self.browser_type.lower() == "chrome":
                options = Options()
                for option in self.chrome_options:
                    options.add_argument(argument=option)
            elif self.browser_type.lower() == "firefox":
                options = FireFox_options()
                for option in self.firefox_options:
                    options.add_argument(argument=option)
            for opt in self.browsers_options:
                if "page_load_strategy" in opt:
                    options.page_load_strategy = opt['page_load_strategy']
                if "browser_name" in opt:
                    options.browser_name = opt['browser_name']

            return options

        except Exception:
            logger.error(f"Getting browser options failed {traceback.format_exc()}")

    def get_chosen_driver_and_config(self) -> webdriver:
        try:
            if self.browser_type.lower() == "chrome":
                return (webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=self._get_browser_options()
                ), self.config)
            elif self.browser_type.lower() == "firefox":
                return (webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install()),
                    options=self._get_browser_options()
                ), self.config)
            else:
                logger.error(
                    f"Driver is not found for browser {self.browser_type}. "
                    f"Probably browser is not supported. Check config.json and class documentation."
                )
        except WebDriverException:
            logger.error(f"Getting driver error {traceback.format_exc()}")
