from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EX.presence_of_element_located(locator)
        )

    def click_element(self, locator, time=5):
        element = self.find_element(locator, time)
        element.click()

    def send_keys(self, locator, keys, time=5):
        element = self.find_element(locator, time)
        element.send_keys(keys)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_to_element_clickable(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EX.element_to_be_clickable(locator)
        )

    def wait_for_number_of_windows(self, number, time=5):
        return WebDriverWait(self.driver, time).until(
            EX.number_of_windows_to_be(number)
        )

    def wait_for_url_contains(self, text, time=5):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, time).until(EX.url_contains(text))

    def get_current_url(self):
        return self.driver.current_url
