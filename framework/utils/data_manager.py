import random
from dataclasses import dataclass
import json
import os
from pathlib import Path
from framework.utils.random_data_generator import DataGenerator

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONF_FILE_JSON = os.path.join(BASE_DIR, "framework", "config.json")
TEST_DATA_JSON = os.path.join(BASE_DIR, "framework", "test_data.json")


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
    email_name: str
    email_domain: str
    password: str


class DataManager:

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
            host_url=test_data_from_file['Host_URL'],
        )
        return test_data

    @staticmethod
    def get_game_page_test_data() -> GamePageTestData:
        e_name = DataGenerator().get_rand_valid_email_name()
        e_dom = DataGenerator().get_rand_valid_email_domain()
        password = DataGenerator().get_rand_valid_passw_for_a1qa_task() + random.choice(e_name)
        test_data = GamePageTestData(
            email_name=e_name,
            email_domain=e_dom,
            password=password
        )
        return test_data
