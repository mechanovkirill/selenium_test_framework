from dataclasses import dataclass
import json
import os
from pathlib import Path

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
class TestData:
    host_url: str
    valid_password: str
    invalid_password: str


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

    def get_test_data(self) -> TestData:
        test_data_from_file = self._json_read(TEST_DATA_JSON)
        test_data = TestData(
            host_url=test_data_from_file['Host_URL'],
            valid_password="",
            invalid_password="",
        )

        return test_data
