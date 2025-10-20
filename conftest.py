from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser