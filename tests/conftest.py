import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    with webdriver.Firefox() as browser:
        browser.implicitly_wait(3)
        yield browser

