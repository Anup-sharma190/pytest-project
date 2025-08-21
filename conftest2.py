# conftest.py
import pytest
from selenium import webdriver

# ---------------- Basic Fixture ----------------
@pytest.fixture
def sample_data():
    """Provides sample data for tests"""
    return {"username": "test_user", "password": "secret123"}


# ---------------- Class-Level Fixture ----------------
@pytest.fixture(scope="class")
def class_fixture():
    """Setup & teardown for a test class"""
    print("\n[SETUP] Running class-level fixture")
    yield
    print("\n[TEARDOWN] Finished class-level fixture")


# ---------------- Cross-Browser Fixture ----------------
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
