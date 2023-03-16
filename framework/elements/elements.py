import traceback
from selenium.common import WebDriverException
from framework.elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond
import logging

logger = logging.getLogger(__name__)


class Element(BaseElement):
    pass


class Button(BaseElement):

    def is_enabled(self) -> bool:
        try:
            logger.info(f"Try is_enabled to {self.name}")
            return WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator)).is_enabled
        except WebDriverException:
            logger.warning(f" is_enabled {self.name} failed  {traceback.format_exc()}")
