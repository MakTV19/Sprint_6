import allure
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators

@allure.title('Тесты на проверку редиректов')
class TestRedirectsPage:

    @allure.title('Тест перехода по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver, redirects_page):
        redirects_page.click_scooter_logo()
        assert redirects_page.is_element_displayed(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)


    @allure.title('Тест перехода по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver, redirects_page):
        redirects_page.click_yandex_logo()
        redirects_page.switch_to_new_window()
        redirects_page.wait.until(expected_conditions.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url

