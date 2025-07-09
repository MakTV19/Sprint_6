import allure
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage

@allure.title('Тесты на проверку редиректов')
class TestRedirectsPage:

    @allure.title('Тест перехода по логотипу Самоката')
    def test_scooter_logo_redirect(self, redirects_page):
        redirects_page.click_scooter_logo()
        assert redirects_page.is_element_displayed(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)

    @allure.title('Тест перехода по логотипу Яндекса')
    def test_yandex_logo_redirect(self, redirects_page):
        redirects_page.click_yandex_logo()
        redirects_page.switch_to_last_window()
        redirects_page.wait_for_url_to_contain("dzen.ru")
        assert redirects_page.current_url_contains("dzen.ru")

