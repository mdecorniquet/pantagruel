import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    with webdriver.Firefox() as browser:
        yield browser

