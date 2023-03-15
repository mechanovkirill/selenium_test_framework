from framework.elements.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond


class Element(BaseElement):
    pass


class Button(BaseElement):

    def is_enabled(self) -> bool:
        """Returns whether the element is enabled."""
        return WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator)).is_enabled
