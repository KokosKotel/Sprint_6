import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class OrderPage:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    COLOR = (By.XPATH, "//input[@id='black']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    CONFIRM_BUTTON = (By.XPATH, "(//button[contains(text(), 'Да')])[1]")
    SUCCESS_POPUP = (By.XPATH, "//div[text()='Заказ оформлен']")

    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, first_name, last_name, address, metro, phone, date, rental_period, color, comment):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.METRO_STATION).send_keys(metro)
        pyautogui.press("down")
        pyautogui.press("enter")
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            EX.presence_of_element_located(self.DATE)
        )
        self.driver.find_element(*self.DATE).send_keys(date)
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        self.driver.find_element(By.XPATH, f"//div[text()='{rental_period}']").click()
        self.driver.find_element(*self.COLOR).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)
        self.driver.find_element(*self.ORDER_BUTTON).click()
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def is_success_popup_present(self):
        return WebDriverWait(self.driver, 3).until(
            EX.presence_of_element_located(self.SUCCESS_POPUP)
        ).is_displayed()
