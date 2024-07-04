from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class MainPage:
    ORDER_TOP_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g')])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    ORDER_FORM = (By.XPATH, "//div[contains(text(),'Для кого самокат')]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        self.driver = driver

    def get_question_heading(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def get_guestion_panel(self, index):
        return (By.ID, f"accordion__panel-{index}")

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 3).until(
            EX.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, index):
        heading_locator = self.get_question_heading(index)
        self.scroll_to_element(heading_locator)
        WebDriverWait(self.driver, 3).until(
            EX.element_to_be_clickable(heading_locator)
        ).click()

    def get_question_panel_text(self, index):
        panel_locator = self.get_guestion_panel(index)
        return self.driver.find_element(*panel_locator).text

    def click_order_top_button(self):
        self.driver.find_element(*self.ORDER_TOP_BUTTON).click()

    def click_order_bottom_button(self):
        order_button_bottom = self.driver.find_element(*self.ORDER_BOTTOM_BUTTON)
        self.scroll_to_element(order_button_bottom)
        order_button_bottom.click()

    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
