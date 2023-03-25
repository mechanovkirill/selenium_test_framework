import random

from framework.base_form import BaseForm
from selenium.webdriver.common.by import By
from framework.elements.elements import Button, Span, Link, MultipleCheckboxes
from framework.utils.data_manager import DataManager


class GamePageCardTwo(BaseForm):
    UPLOAD_IMAGE_LINK = (By.XPATH, "//a[contains(@class, 'avatar') and text()='upload']")
    UNSELECT_ALL_CHECKBOX = (By.XPATH, "//label[@for='interest_unselectall']//span[contains(@class, 'icon')]")
    ALL_CHECKBOXES = (By.XPATH, "//span[@class='checkbox__box']")
    NEXT_BUTTON_CARD_2 = (By.XPATH, "//button[@name='button' and text()='Next']")
    CARD_3_IS_UNIQUE_LOCATOR = (By.XPATH, "//div[contains(@class, 'toggle-button') and text()='Male']")

    def __init__(self) -> None:
        super().__init__(
            unique_locator=(By.XPATH, "//button[@name='button' and text()='Download image']"),
            name='Game Page(card 1)'
        )
        self.test_data = DataManager().get_game_page_test_data()
        # elements:
        self.upload_image_link = Link(self.UPLOAD_IMAGE_LINK, 'Upload image link')
        self.unselect_all_checkbox = Span(self.UNSELECT_ALL_CHECKBOX, 'Checkbox unselect all')
        self.all_checkboxes = MultipleCheckboxes(self.ALL_CHECKBOXES, 'All card 2 checkboxes')
        self.next_button_card_2 = Button(self.NEXT_BUTTON_CARD_2, 'Next button card 2')
        self.card_3_unique_locator = Button(self.CARD_3_IS_UNIQUE_LOCATOR, 'card_3_unique_locator')

    def upload_valid_image(self) -> None:
        image = self.test_data.image
        self.upload_image_link.click()
        self.browser.paste_text_into_active_window_field_and_enter_via_pyautogui(image)

    def select_3_checkboxes(self) -> None:
        self.unselect_all_checkbox.click()
        all_checkboxes = self.all_checkboxes.find_visible_elements()
        three_rand_digit = set()

        while len(three_rand_digit) != 3:
            li = random.choices([x for x in range(len(all_checkboxes) - 1)], k=3)
            if 17 in li:
                continue
            three_rand_digit = set(li)

        for i in three_rand_digit:
            all_checkboxes[i].click()

    def click_to_the_card_2_next_button(self) -> None:
        self.next_button_card_2.click()

    def card_3_is_open(self) -> bool:
        return self.card_3_unique_locator.is_displayed()
