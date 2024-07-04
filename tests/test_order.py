import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from constants import ConstantsURL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Тест кнопки заказа")
@allure.story("Верхняя кнопка заказа")
@allure.title("Тест верхней кнопки заказа")
@allure.description("Тест проверяет работоспособность верхней кнопки 'Заказать'")
def test_order_top_button(driver):
    main_page = MainPage(driver)
    main_page.click_order_top_button()
    assert "order" in driver.current_url

@allure.feature("Тест кнопки заказа")
@allure.story("Нижняя кнопка заказа")
@allure.title("Тест нижней кнопки заказа")
@allure.description("Тест проверяет работоспособность нижней кнопки 'Заказать'")
def test_order_bottom_button(driver):
    main_page = MainPage(driver)
    main_page.click_order_bottom_button()
    assert "order" in driver.current_url

@allure.feature("Тест заказа")
@allure.story("Позитивный сценарий заказа")
@allure.title("Тест позитивного сценария заказа")
@allure.description("Тест проверяет заполнение формы заказа и появление сообщения об успешном заказе")
@pytest.mark.parametrize("first_name, last_name, address, metro, phone, date, rental_period, color, comment", [
    ("Иосиф", "Бродский", "ул. Рылеева, д. 2", "Чистые пруды", "91231231239", "31.12.2024", "трое суток", "black", "Позвонить за полчаса"),
    ("Стив", "Джобс", "ул. Ленина, д. 50", "Ленинский проспект", "93213213219", "30.11.2024", "сутки", "grey", "-")
])
def test_order_positive(driver, first_name, last_name, address, metro, phone, date, rental_period, color, comment):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.click_order_top_button()
    order_page.fill_order_form(first_name, last_name, address, metro, phone, date, rental_period, color, comment)
    assert order_page.is_success_popup_present()

@allure.feature("Тест клик по логотипу")
@allure.story("Клик по логотипу 'Самоката'")
@allure.title("Тест клика по логотипу 'Самоката'")
@allure.description("Тест проверяет что при клике на логотип 'Самоката' из формы заказа, перенаправляет на главную страницу")
def test_click_scooter_logo(driver):
    main_page = MainPage(driver)
    main_page.click_order_top_button()
    main_page.click_scooter_logo()
    assert driver.current_url == ConstantsURL.scooter_URL

@allure.feature("Тест клик по логотипу")
@allure.story("Клик по логотипу 'Яндекс'")
@allure.title("Тест клика по логотипу 'Яндекс'")
@allure.description("Тест проверяет что при клике на логотип 'Яндекса', открывается новая вкладка с главной страницей Яндекс.Дзен")
def test_click_yandex_logo(driver):
    main_page = MainPage(driver)
    main_page.click_yandex_logo()
    WebDriverWait(driver, 3).until(EX.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 3).until(EX.url_contains("dzen.ru"))
    assert "dzen.ru" in driver.current_url
