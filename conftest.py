import pytest
from selenium import webdriver
from constants import ConstantsURL


@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.get(ConstantsURL.scooter_URL)
    yield browser

    browser.quit()
