import random
from dataclasses import dataclass
import json
import os
from pathlib import Path
from framework.utils.random_data_generator import DataGenerator

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONF_FILE_JSON = os.path.join(BASE_DIR, "config.json")
TEST_DATA_JSON = os.path.join(BASE_DIR, "test_project", "tests", "test_data", "test_data.json")


@dataclass
class ConfigData:
    browser: str
    browsers_options: tuple[dict]
    chrome_options: tuple[str]
    firefox_options: tuple[str]

    timeout: float
    poll_frequency: float

    debug: str


@dataclass
class MainPageTestData:
    host_url: str


@dataclass
class GamePageTestData:
    valid_rand_email_name: str
    valid_rand_email_domain: str
    valid_rand_password: str
    invalid_passwords: list[str]


class DataManager:
    """DataManager read data from json files, put data to dataclasses
    and hand over dataclasses to other project entities."""

    @staticmethod
    def _json_read(json_file: str) -> dict:
        with open(json_file, 'r') as file:
            result = json.load(file)
        return result

    def get_config_data(self) -> ConfigData:
        conf_data = self._json_read(CONF_FILE_JSON)
        config = ConfigData(
            browser=conf_data['Browser'],
            browsers_options=tuple(conf_data['Common_browsers_options']),
            chrome_options=tuple(conf_data['Chrome_options']),
            firefox_options=tuple(conf_data['Firefox_options']),
            timeout=conf_data['Explicit_wait_timeout'],
            poll_frequency=conf_data['Explicit_wait_poll_frequency'],
            debug=conf_data['Debug'],
        )
        return config

    def get_main_page_test_data(self) -> MainPageTestData:
        test_data_from_file = self._json_read(TEST_DATA_JSON)
        test_data = MainPageTestData(
            host_url=test_data_from_file["main_page_test_data"]['Host_URL'],
        )
        return test_data

    @staticmethod
    def get_game_page_test_data() -> GamePageTestData:
        e_name = DataGenerator().get_rand_valid_email_name()
        e_dom = DataGenerator().get_rand_valid_email_domain()
        password = DataGenerator().get_rand_valid_password_for_a1qa_task() + random.choice(e_name)
        invalid_password = DataGenerator().get_list_of_invalid_rand_passwords()
        # add email character to passwords
        for s in range(len(invalid_password)):
            if s == 3:
                for ch in e_name:
                    if ch not in '0123456789':
                        invalid_password[s] += ch
                        continue
            if s == 4:
                for ch in e_name:
                    if ch not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        invalid_password[s] += ch
                        continue
            if s == 5:
                invalid_password[s] += e_name[0]
                break
        # remove email characters out of one password to do it invalid
        for char in invalid_password[6]:
            if char in e_name:
                invalid_password[6] = invalid_password[6].replace(char, '1A')

        test_data = GamePageTestData(
            valid_rand_email_name=e_name,
            valid_rand_email_domain=e_dom,
            valid_rand_password=password,
            invalid_passwords=invalid_password,
        )
        return test_data
