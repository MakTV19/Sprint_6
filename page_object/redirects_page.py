import allure
from page_object.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class RedirectsPage(BasePage):

    @allure.step('Нажимаем на SCOOTER Logo')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажимаем на YANDEX Logo')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)