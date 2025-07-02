import allure
from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num + 1)
        self.scroll_to_element(locator_q_formatted)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num + 1)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Кликаем на логотип Самоката')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)
