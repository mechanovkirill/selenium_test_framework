import pytest
from framework.browsers.browser import Browser


@pytest.fixture(scope='function', autouse=True)
def driver_quit():
    """Maximize the browsers window when running each test and exit the driver after each test"""
    Browser().get_driver().maximize_window()
    yield
    Browser().quit()
