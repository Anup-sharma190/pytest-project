# tests/test_crossbrowser.py
import pytest

def test_google_title(cross_browser):
    driver = cross_browser
    driver.get("https://www.google.com")
    assert "Google" in driver.title
