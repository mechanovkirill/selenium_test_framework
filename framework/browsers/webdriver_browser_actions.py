from selenium.webdriver import ActionChains
from selenium.webdriver.remote import webelement


class WebdriverBrowserActions:
    def __init__(self, driver_):
        self.driver = driver_

    def scroll_to_element(self, webelement_: webelement) -> None:
        ActionChains(self.driver) \
            .scroll_to_element(webelement_) \
            .perform()
