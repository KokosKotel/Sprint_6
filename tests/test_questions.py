import allure
from constants import ConstantsTextQuestion
from pages.main_page import MainPage

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 1")
@allure.title("Тест 1 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_1(driver):
    main_page = MainPage(driver)
    main_page.click_question(0)
    panel_text = main_page.get_question_panel_text(0)
    assert panel_text == ConstantsTextQuestion.question_texts[0]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 2")
@allure.title("Тест 2 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_2(driver):
    main_page = MainPage(driver)
    main_page.click_question(1)
    panel_text = main_page.get_question_panel_text(1)
    assert panel_text == ConstantsTextQuestion.question_texts[1]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 3")
@allure.title("Тест 3 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_3(driver):
    main_page = MainPage(driver)
    main_page.click_question(2)
    panel_text = main_page.get_question_panel_text(2)
    assert panel_text == ConstantsTextQuestion.question_texts[2]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 4")
@allure.title("Тест 4 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_4(driver):
    main_page = MainPage(driver)
    main_page.click_question(3)
    panel_text = main_page.get_question_panel_text(3)
    assert panel_text == ConstantsTextQuestion.question_texts[3]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 5")
@allure.title("Тест 5 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_5(driver):
    main_page = MainPage(driver)
    main_page.click_question(4)
    panel_text = main_page.get_question_panel_text(4)
    assert panel_text == ConstantsTextQuestion.question_texts[4]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 6")
@allure.title("Тест 6 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_6(driver):
    main_page = MainPage(driver)
    main_page.click_question(5)
    panel_text = main_page.get_question_panel_text(5)
    assert panel_text == ConstantsTextQuestion.question_texts[5]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 7")
@allure.title("Тест 7 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_7(driver):
    main_page = MainPage(driver)
    main_page.click_question(6)
    panel_text = main_page.get_question_panel_text(6)
    assert panel_text == ConstantsTextQuestion.question_texts[6]

@allure.feature("Раздел 'Вопросы о важном'")
@allure.story("Вопрос 8")
@allure.title("Тест 8 вопроса")
@allure.description("Тест проверяет отображаемый текст вопроса")
def test_question_8(driver):
    main_page = MainPage(driver)
    main_page.click_question(7)
    panel_text = main_page.get_question_panel_text(7)
    assert panel_text == ConstantsTextQuestion.question_texts[7]
