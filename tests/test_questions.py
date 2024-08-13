import allure
import pytest
from constants import ConstantsTextQuestion
from pages.main_page import MainPage


@allure.feature("Тест раздела Вопросы о важном")
class TestQuestions:
    @allure.title("Тест вопросов")
    @allure.description("Тест проверяет отображаемый текст вопроса")
    @pytest.mark.parametrize("question_index, expected_text", [
        (0, ConstantsTextQuestion.question_texts[0]),
        (1, ConstantsTextQuestion.question_texts[1]),
        (2, ConstantsTextQuestion.question_texts[2]),
        (3, ConstantsTextQuestion.question_texts[3]),
        (4, ConstantsTextQuestion.question_texts[4]),
        (5, ConstantsTextQuestion.question_texts[5]),
        (6, ConstantsTextQuestion.question_texts[6]),
        (7, ConstantsTextQuestion.question_texts[7])
    ])
    def test_questions(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.click_question(question_index)
        panel_text = main_page.get_question_panel_text(question_index)
        assert panel_text == expected_text
