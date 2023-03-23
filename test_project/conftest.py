import datetime
import os
import pytest
from framework.browsers.browser import Browser
from framework.utils.data_manager import BASE_DIR


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    result_setup - setup result
    result_call - test result
    result_teardown - teardown result
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "result_" + rep.when, rep)


@pytest.fixture(scope='function', autouse=True)
def main_fixture(request):
    Browser().get_driver().maximize_window()
    yield
    if request.node.result_call.outcome == "failed":
        date_time = request.node.name, datetime.datetime.now()
        path_filename = os.path.join(
            BASE_DIR, 'test_project', 'screenshots', f'{date_time}.png'
        )
        Browser().take_screenshot(path_filename)
    Browser().quit()
