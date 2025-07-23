import pytest
from selenium import webdriver
from page_object.main_page import MainPage
from page_object.order_page import OrderPage
from page_object.redirects_page import RedirectsPage
import data

Browser_name = None


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(data.URL_MAIN_PAGE)
    return page

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def redirects_page(driver):
    page = RedirectsPage(driver)
    page.go_to_url(data.URL_MAIN_PAGE)
    return page
