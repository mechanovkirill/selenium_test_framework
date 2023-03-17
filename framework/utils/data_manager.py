import dataclasses
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
conf_file_json = os.path.join(BASE_DIR, "framework", "config.json")

with open(conf_file_json) as conf:
    config = json.load(conf)


@dataclasses.dataclass
class ConfigData:
    host_url: str = config['Host_URL']
    time: float = config['Explicit_wait_time']
    browser: str = config['Browser']
    browsers_options: tuple[dict] = tuple(config['Common_browsers_options'])
    chrome_options: tuple[str] = tuple(config['Chrome_options'])
    firefox_options: tuple[str] = tuple(config['Firefox_options'])
    debug: str = config['Debug']
