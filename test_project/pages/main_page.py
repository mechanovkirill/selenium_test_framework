from framework.base_form import BaseForm
from selenium.webdriver.common.by import By
from framework.elements.elements import Link

from framework.utils.data_manager import DataManager


class MainPage(BaseForm):
    HERE_LINK_LOCATOR = (By.XPATH, "//a[@class='start__link' and (@href='/game.html' or contains(text(), 'HERE'))]")

    def __init__(self) -> None:
        super().__init__(
            unique_locator=(By.XPATH, "//a[@class='start__link' and (@href='/game.html' or contains(text(), 'HERE'))]"),
            name='Main Page'
        )
        self.url = DataManager().get_main_page_test_data().host_url
        # elements:
        self.here_link = Link(self.HERE_LINK_LOCATOR, 'Here Link')

    def open(self) -> None:
        self.driver.get(self.url)

    def click_to_here_link(self) -> None:
        self.here_link.click()
