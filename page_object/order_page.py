import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from page_object.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class OrderPage(BasePage):

    @allure.step('Заполняем форму заказа')
    def set_order(self, data):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, data['name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, data['address'])

        self.click_to_element(OrderPageLocators.STATION_INPUT_LOCATOR)
        station_locator = (By.XPATH, f'//div[text()="{data["station"]}"]')
        self.wait.until(expected_conditions .visibility_of_element_located(station_locator))
        self.click_to_element(station_locator)


        self.add_text_to_element(OrderPageLocators.NUMBER_LOCATOR, data['number'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)

        self.add_text_to_element(OrderPageLocators.DATE_INPUT_LOCATOR, data['date'])

        action = ActionChains(self.driver)
        action.move_by_offset(0, 0).click().perform()

        self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocators.RENT_DROPDOWN_LOCATOR))
        self.click_to_element(OrderPageLocators.RENT_DROPDOWN_LOCATOR)

        rent_day_locator = (By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{data["rental_time"]}"]')
        self.wait.until(expected_conditions.element_to_be_clickable(rent_day_locator))
        self.click_to_element(rent_day_locator)

        if data['color'] == 'black':
            self.click_to_element(OrderPageLocators.COLOR_BLACK_LOCATOR)
        elif data['color'] == 'grey':
            self.click_to_element(OrderPageLocators.COLOR_GREY_LOCATOR)

        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, data['comment'])
        self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocators.FINAL_ORDER_BUTTON_LOCATOR))
        self.click_to_element(OrderPageLocators.FINAL_ORDER_BUTTON_LOCATOR)

        self.wait.until(expected_conditions.visibility_of_element_located(OrderPageLocators.CONFIRM_BUTTON_LOCATOR))
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON_LOCATOR)

        self.wait.until(expected_conditions.element_to_be_clickable(OrderPageLocators.STATUS_BUTTON_LOCATOR))
        self.click_to_element(OrderPageLocators.STATUS_BUTTON_LOCATOR)

    def check_order(self, locator):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
            return True
        except:
            return False


