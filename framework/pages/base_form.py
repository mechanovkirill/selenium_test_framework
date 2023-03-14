from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond


class BaseForm:
    def __init__(self, name: str, unique_locator: tuple[any, str]) -> None:
        self.name = name
        self.unique_locator = unique_locator
        self.driver = None

    def is_open(self) -> bool:  # TODO: timeout
        is_opened = WDWait(self.driver, 10).until(
            exp_cond.visibility_of_element_located(self.unique_locator)
        ).is_displayed()
        return is_opened
