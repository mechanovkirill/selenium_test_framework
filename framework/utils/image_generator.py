from PIL import Image
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def create_image(size: tuple[int, int], color_: tuple[int, int, int]) -> str:
    image = Image.new('RGB', size, color=color_)

    path = os.path.join(BASE_DIR, "test_project", "tests", "test_data", "image.png")
    if os.path.exists(path):
        return path
    else:
        image.save(os.path.join(BASE_DIR, "test_project", "tests", "test_data", "image.png"))
        path = os.path.join(BASE_DIR, "test_project", "tests", "test_data", "image.png")
        return path
