import pytest
import allure
from data import answers_data

@allure.title('Тесты на проверку вопросов')
class TestMainPage:

    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions_and_answers(self, num, main_page):
        assert main_page.check_question_and_answer(num) == answers_data[num]
