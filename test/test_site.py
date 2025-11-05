from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage


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
    WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '.card'))
    )
    homepage.check_product_count(2)
