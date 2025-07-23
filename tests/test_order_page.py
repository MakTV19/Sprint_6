import pytest
import allure
import data


class TestOrderPage:

    @allure.title('Создание заказа через верхнюю и нижнюю кнопку')
    @pytest.mark.parametrize(
        'order_entry_point, order_data',
        [
            ("top_button", data.ORDER_DATA_1),
            ("bottom_button", data.ORDER_DATA_2)
        ]
    )
    def test_create_order(self, main_page, order_page, order_entry_point, order_data):
        main_page.start_order_from(order_entry_point)
        order_page.set_order(order_data)
        assert order_page.is_order_successful()