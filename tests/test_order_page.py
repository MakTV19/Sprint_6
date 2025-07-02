import pytest
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import data


@allure.title('Тесты оформления заказа с разными точками входа')
class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_UP, data.ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_DOWN, data.ORDER_DATA_2)
        ]
    )
    def test_create_order(self, main_page, order_page, locator, order_data):
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        order_page.set_order(order_data)
        assert order_page.check_order(OrderPageLocators.STATUS_TITLE_LOCATOR)