from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, driver, locator: tuple, name: str):
        self.locator = locator
        self.name = name
        self.driver = driver

    def _get_element(self) -> WebElement:
        return self.driver.find_element(self.locator)

    def click(self):
        # logger.info(f"{self.name}") #  TODO:log
        WDWait(self.driver, 10).until(exp_cond.element_to_be_clickable(self.locator)).click()

    def get_attribute(self, attribute):
        WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator)).get_attribute(attribute)

    def get_property(self, property_):
        WDWait(self.driver, 10).until(exp_cond.presence_of_element_located(self.locator)).get_property(property_)
