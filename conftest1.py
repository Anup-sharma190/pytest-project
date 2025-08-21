# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def cross_browser(request):
    """Fixture to run tests on multiple browsers"""
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser!")

    driver.maximize_window()
    yield driver
    driver.quit()
