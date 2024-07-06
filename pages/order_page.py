import allure
import pyautogui
from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
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

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, first_name, last_name, address, metro, phone, date, rental_period, comment):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.ADDRESS, address)
        self.send_keys(self.METRO_STATION, metro)
        pyautogui.press("down")
        pyautogui.press("enter")
        self.send_keys(self.PHONE_NUMBER, phone)
        self.click_element(self.NEXT_BUTTON)
        self.send_keys(self.DATE, date)
        self.click_element(self.RENTAL_PERIOD)
        self.click_element((By.XPATH, f"//div[text()='{rental_period}']"))
        self.click_element(self.COLOR)
        self.send_keys(self.COMMENT, comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Проверяем отображение сообщения об успешном заказе")
    def is_success_popup_present(self):
        return self.find_element(self.SUCCESS_POPUP) is not None
