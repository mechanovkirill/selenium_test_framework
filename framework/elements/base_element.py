from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, driver, locator: tuple[By, str], name: str):
        self.locator = locator
        self.name = name
        self.driver = driver

    def _find_element(self) -> WebElement:
        return WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator))

    def click(self) -> None:
        if WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator)).is_enabled():
            # logger.info(f"{self.name}") #  TODO:log
            WDWait(self.driver, 10).until(exp_cond.element_to_be_clickable(self.locator)).click()
        else:
            # logger.error
            pass

    def is_displayed(self) -> bool:
        return WDWait(self.driver, 10).until(exp_cond.visibility_of_element_located(self.locator)).is_displayed()

    def get_attribute(self, attribute: str) -> str:
        return self._find_element().get_attribute(attribute)

    def get_property(self, property_: str) -> str:
        return self._find_element().get_property(property_)

    def get_text(self) -> str:
        return self._find_element().text
