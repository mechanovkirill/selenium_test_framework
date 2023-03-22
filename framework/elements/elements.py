import traceback
from selenium.common import WebDriverException
from framework.elements.base_element import BaseElement
import logging

logger = logging.getLogger(__name__)


class Link(BaseElement):
    pass


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
            logger.info(f'| {self.name} keys was sent: {value.encode("utf8")}.')
        except WebDriverException:
            logger.warning(f'| Filling the fill failed to {self.name} {traceback.format_exc()}.')


class Span(BaseElement):
    pass
