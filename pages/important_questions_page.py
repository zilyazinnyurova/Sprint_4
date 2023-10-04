from locators.important_questions_locators import Locators
from base_page import BasePage
import allure


class ImportantQuestionsPage(BasePage):

    @allure.step('Скролим к блоку с вопросами')
    def scroll_to_questions_block(self):
        self.scroll_to_element(Locators.important_questions)

    @allure.step('Кликаем на кнопку с вопросом')
    def click_to_question_button(self, button_locator):
        self.wait_presence_of_element(button_locator)
        self.click_on_unclickable_element(button_locator)

    @allure.step('Получаем ответ')
    def get_answer(self, answer_locator):
        self.wait_visibility_of_element(answer_locator)
        return self.get_text(answer_locator)
