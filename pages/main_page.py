import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    ORDER_TOP_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g')])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def get_question_heading(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def get_question_panel(self, index):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step("Нажимаем на вопрос номер {index}")
    def click_question(self, index):
        heading_locator = self.get_question_heading(index)
        self.scroll_to_element(heading_locator)
        self.click_element(heading_locator)

    @allure.step("Получаем текст ответа на вопрос номер {index}")
    def get_question_panel_text(self, index):
        panel_locator = self.get_question_panel(index)
        return self.find_element(panel_locator).text

    @allure.step("Нажимаем верхнюю кнопку 'Заказать'")
    def click_order_top_button(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    @allure.step("Нажимаем нижнюю кнопку 'Заказать'")
    def click_order_bottom_button(self):
        self.scroll_to_element(self.ORDER_BOTTOM_BUTTON)
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    @allure.step("Нажимаем на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Нажимаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
