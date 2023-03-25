import traceback
from selenium.common import WebDriverException
from selenium.webdriver.remote import webelement
from framework.elements.base_element import BaseElement
import logging

logger = logging.getLogger(__name__)


class BaseMultipleElements(BaseElement):
    def find_visible_elements(self) -> list[webelement]:
        try:
            elements = self.wait_for.visibility_of_all_elements_located(self.locator)
            logger.info(f"| Visible elements {self.name} are find.")
            return elements
        except WebDriverException:
            logger.warning(f"| Method find_visible_elements {self.name} failed {traceback.format_exc()}")


class Link(BaseElement):
    def send_keys(self, value: str | float) -> None:
        try:
            self.wait_for.visibility_of_element_located(self.locator, self.name).send_keys(value)
            logger.info(f'| {self.name} the following keys was sent: {value.encode("utf8")}.')
        except WebDriverException:
            logger.warning(f'| Keys sending failed to {self.name} {traceback.format_exc()}.')


class Button(BaseElement):
    pass


class Div(BaseElement):
    pass


class Input(BaseElement):
    def clear(self) -> None:
        try:
            self.wait_for.visibility_of_element_located(self.locator, self.name).clear()
            logger.info(f'| {self.name} text cleared.')
        except WebDriverException:
            logger.warning(f'| Clearing text failed to {self.name} {traceback.format_exc()}.')

    def fill_the_field(self, value: str | float) -> None:
        try:
            self.wait_for.visibility_of_element_located(self.locator, self.name).send_keys(value)
            logger.info(f'| {self.name} the following keys was sent: {value.encode("utf8")}.')
        except WebDriverException:
            logger.warning(f'| Filling the fill failed to {self.name} {traceback.format_exc()}.')


class Span(BaseElement):
    pass


class MultipleDivs(BaseMultipleElements):
    pass


class MultipleCheckboxes(BaseMultipleElements):
    def is_selected(self) -> bool:
        try:
            is_selected = self.wait_for.visibility_of_all_elements_located(self.locator).is_selected()
            logger.info(f"| Method is_selected applied to {self.name}.")
            return is_selected
        except WebDriverException:
            logger.warning(f"| Method is_selected {self.name} failed {traceback.format_exc()}")
