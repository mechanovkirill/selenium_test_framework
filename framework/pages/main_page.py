from framework.utils.config_data import ConfigData
from framework.pages.base_form import BaseForm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.support import expected_conditions as exp_cond

config = ConfigData()


class MainPage(BaseForm):
    def __init__(self, driver) -> None:
        super().__init__(
            name='main page',
            unique_locator=(By.XPATH, "//a[@class='start__link' and (@href='/game.html' or contains(text(), 'HERE'))]"),
        )
        self.driver = driver
        self.url = config.host_url

    HERE_LINK_LOCATOR = (By.XPATH, "//a[@class='start__link' and (@href='/game.html' or contains(text(), 'HERE'))]")

    def open(self) -> None:
        self.driver.get(self.url)

    def click_to_here_link(self) -> None:
        WDWait(self.driver, 10).until(
            exp_cond.visibility_of_element_located(self.HERE_LINK_LOCATOR)
        ).click()
