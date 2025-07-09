from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        time.sleep(0.3)
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def scroll_to_element(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(expected_conditions.visibility_of(element))
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(expected_conditions.url_changes(self.driver.current_url))

    def is_element_displayed(self, locator):
        try:
            return self.find_element_with_wait(locator).is_displayed()
        except:
            return False

    def current_url_contains(self, text):
        return text in self.driver.current_url

    def wait_for_url_to_contain(self, text):
        self.wait.until(expected_conditions.url_contains(text))


