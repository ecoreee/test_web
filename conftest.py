from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
