from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '(//div[@class="accordion__button"])[{}]'
    ANSWER_LOCATOR = By.XPATH, '(//div[@class="accordion__panel"])[{}]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '(//div[@class="accordion__button"])[last()]'

    ORDER_BUTTON_UP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_DOWN = (By.XPATH, "(//button[text()='Заказать'])[last()]")

    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    REDIRECT_URL = "https://dzen.ru/"
