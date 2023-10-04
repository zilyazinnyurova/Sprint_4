from pages.important_questions_page import ImportantQuestionsPage
from locators.important_questions_locators import Locators
from data.answers_data import AnswersData
import allure
import pytest


class TestPraktikumScooter:

    @pytest.mark.parametrize('questions_block', [
        {'button_locator': Locators.button_question_of_cost,
         'text_locator': Locators.text_for_cost,
         'expected_text': AnswersData.cost_answer
         },
        {'button_locator': Locators.button_question_of_multiple_scooters,
         'text_locator': Locators.text_for_multiple_scooters,
         'expected_text': AnswersData.many_scooters
         },
        {'button_locator': Locators.button_question_of_rental_time,
         'text_locator': Locators.text_for_rental_time,
         'expected_text': AnswersData.rental_time
         },
        {'button_locator': Locators.button_question_of_order_for_today,
         'text_locator': Locators.text_for_order_for_today,
         'expected_text': AnswersData.order_for_today
         },
        {'button_locator': Locators.button_question_of_order_extension,
         'text_locator': Locators.text_for_order_extension,
         'expected_text': AnswersData.order_extension
         },
        {'button_locator': Locators.button_question_of_charging,
         'text_locator': Locators.text_for_charging,
         'expected_text': AnswersData.charging
         },
        {'button_locator': Locators.button_question_of_order_cancel,
         'text_locator': Locators.text_for_order_cancel,
         'expected_text': AnswersData.order_cancel
         },
        {'button_locator': Locators.button_question_of_order_outside_mkad,
         'text_locator': Locators.text_for_order_outside_mkad,
         'expected_text': AnswersData.order_outside_mkad
         }
    ])
    @allure.description("Кликнуть на вопрос и получить ответ")
    def test_click_on_questions(self, driver, questions_block):
        important_on_page = ImportantQuestionsPage(driver)

        important_on_page.scroll_to_questions_block()
        important_on_page.click_to_question_button(questions_block['button_locator'])
        answer = important_on_page.get_answer(questions_block['text_locator'])
        assert answer == questions_block['expected_text']
