from framework.elements.base_element import BaseElement
from selenium.common import WebDriverException
import logging

logger = logging.getLogger(__name__)


class JSActions:
    def __init__(self, driver_):
        self.driver = driver_

    def scroll_into_view(self, element: BaseElement):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element.locator))
            logger.info(f"| Scrolled into view {element.name}")
        except WebDriverException:
            logger.error(f"| Scrolling into view {element.name} failed")
