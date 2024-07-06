import allure
import pytest
from constants import ConstantsURL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Тест кнопки заказа")
class TestOrderButton:
    @allure.title("Тест верхней кнопки заказа")
    @allure.description("Тест проверяет работоспособность верхней кнопки 'Заказать'")
    def test_order_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_top_button()
        assert "order" in main_page.get_current_url()


    @allure.title("Тест нижней кнопки заказа")
    @allure.description("Тест проверяет работоспособность нижней кнопки 'Заказать'")
    def test_order_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_bottom_button()
        assert "order" in main_page.get_current_url()


@allure.feature("Тест формы заказа")
class TestFillOrderForm:
    @allure.title("Тест позитивного сценария заказа")
    @allure.description("Тест проверяет заполнение формы заказа и появление сообщения об успешном заказе")
    @pytest.mark.parametrize("first_name, last_name, address, metro, phone, date, rental_period, comment", [
        ("Иосиф", "Бродский", "ул. Рылеева, д. 2", "Чистые пруды", "91231231239", "31.12.2024", "трое суток", "Позвонить за полчаса"),
        ("Стив", "Джобс", "ул. Ленина, д. 50", "Ленинский проспект", "93213213219", "30.11.2024", "сутки", "-")
    ])
    def test_order_positive(self, driver, first_name, last_name, address, metro, phone, date, rental_period, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_top_button()
        order_page.fill_order_form(first_name, last_name, address, metro, phone, date, rental_period, comment)
        assert order_page.is_success_popup_present()


@allure.feature("Тест клика по логотипам")
class TestClickLogo:
    @allure.title("Тест клика по логотипу 'Самоката'")
    @allure.description("Тест проверяет что при клике на логотип 'Самоката' из формы заказа, перенаправляет на главную страницу")
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_top_button()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == ConstantsURL.scooter_URL


    @allure.title("Тест клика по логотипу 'Яндекс'")
    @allure.description("Тест проверяет что при клике на логотип 'Яндекса', открывается новая вкладка с главной страницей Яндекс.Дзен")
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.wait_for_number_of_windows(2)
        main_page.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in main_page.get_current_url()
