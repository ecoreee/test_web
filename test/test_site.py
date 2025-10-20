from selenium import webdriver
import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is_title('Samsung galaxy s6')
    

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)  #TODO:
    homepage.chech_product_count(2)
