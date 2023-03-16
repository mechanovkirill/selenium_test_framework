import pytest
from framework.browser import Browser


@pytest.fixture(scope='function', autouse=True)
def driver_quit():
    """Quite driver after every each test"""
    yield
    Browser().quit()
