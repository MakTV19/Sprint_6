from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_LOCATOR = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_LOCATOR = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_LOCATOR = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    STATION_INPUT_LOCATOR = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    NUMBER_LOCATOR = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Далее"]')

    DATE_INPUT_LOCATOR = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_DROPDOWN_LOCATOR = (By.CLASS_NAME, 'Dropdown-control')

    COLOR_BLACK_LOCATOR = (By.ID, 'black')
    COLOR_GREY_LOCATOR = (By.ID, 'grey')

    COMMENT_LOCATOR = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    FINAL_ORDER_BUTTON_LOCATOR = (By.XPATH, "(//button[text()='Заказать'])[last()]")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_HEADER_LOCATOR = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    STATUS_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Посмотреть статус"]')
    STATUS_TITLE_LOCATOR = (By.XPATH, '//div[contains(@class, "Track_Order__") and contains(text(), "Самокат на складе")]')

