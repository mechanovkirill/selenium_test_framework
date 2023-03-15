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
    host_url: str = config['Host URL']
    time: float = config['Explicit_wait_time']
    browser: str = config['Browser']
    debug: str = config['Debug']


