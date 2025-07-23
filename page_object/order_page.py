import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_object.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполняем форму заказа')
    def set_order(self, data):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, data['name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, data['address'])

        self.click_to_element(OrderPageLocators.STATION_INPUT_LOCATOR)
        station_locator = (
            By.XPATH,
            OrderPageLocators.STATION_OPTION_TEMPLATE.format(station=data["station"])
        )
        self.wait_for_visibility(station_locator)
        self.click_to_element(station_locator)

        self.add_text_to_element(OrderPageLocators.NUMBER_LOCATOR, data['number'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)

        self.add_text_to_element(OrderPageLocators.DATE_INPUT_LOCATOR, data['date'])
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()

        self.wait_for_clickable(OrderPageLocators.RENT_DROPDOWN_LOCATOR)
        self.click_to_element(OrderPageLocators.RENT_DROPDOWN_LOCATOR)

        rent_day_locator = (
            By.XPATH,
            OrderPageLocators.RENT_DAY_OPTION_TEMPLATE.format(rental_time=data["rental_time"])
        )
        self.wait_for_clickable(rent_day_locator)
        self.click_to_element(rent_day_locator)

        if data['color'] == 'black':
            self.click_to_element(OrderPageLocators.COLOR_BLACK_LOCATOR)
        elif data['color'] == 'grey':
            self.click_to_element(OrderPageLocators.COLOR_GREY_LOCATOR)

        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, data['comment'])

        self.wait_for_clickable(OrderPageLocators.FINAL_ORDER_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.FINAL_ORDER_BUTTON_LOCATOR)

        self.wait_for_visibility(OrderPageLocators.CONFIRM_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON_LOCATOR)

        self.wait_for_clickable(OrderPageLocators.STATUS_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.STATUS_BUTTON_LOCATOR)

    @allure.step('Проверяем, что заказ успешно оформлен')
    def check_order(self, locator):
        try:
            self.wait_for_visibility(locator)
            return True
        except:
            return False