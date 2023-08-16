from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.important_questions_page import ImportantQuestionsPage
from locators.important_questions_locators import Locators


class TestPraktikumScooter:
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    def test_click_on_button_question_of_cost(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_cost)
        important_on_page.click_on_button(Locators.button_question_of_cost)
        important_on_page.wait_for_load_text(Locators.text_for_cost)
        element = important_on_page.get_text(Locators.text_for_cost)
        assert element == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_click_on_button_question_of_multiple_scooters(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_multiple_scooters)
        important_on_page.click_on_button(Locators.button_question_of_multiple_scooters)
        important_on_page.wait_for_load_text(Locators.text_for_multiple_scooters)
        element = important_on_page.get_text(Locators.text_for_multiple_scooters)
        assert element == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'


    def test_click_on_button_question_of_rental_time(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_rental_time)
        important_on_page.click_on_button(Locators.button_question_of_rental_time)
        important_on_page.wait_for_load_text(Locators.text_for_rental_time)
        element = important_on_page.get_text(Locators.text_for_rental_time)
        assert element == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


    def test_click_on_button_question_of_order_for_today(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_order_for_today)
        important_on_page.click_on_button(Locators.button_question_of_order_for_today)
        important_on_page.wait_for_load_text(Locators.text_for_order_for_today)
        element = important_on_page.get_text(Locators.text_for_order_for_today)
        assert element == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'


    def test_click_on_button_question_of_order_extension(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_order_extension)
        important_on_page.click_on_button(Locators.button_question_of_order_extension)
        important_on_page.wait_for_load_text(Locators.text_for_order_extension)
        element = important_on_page.get_text(Locators.text_for_order_extension)
        assert element == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'


    def test_click_on_button_question_of_charging(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_charging)
        important_on_page.click_on_button(Locators.button_question_of_charging)
        important_on_page.wait_for_load_text(Locators.text_for_charging)
        element = important_on_page.get_text(Locators.text_for_charging)
        assert element == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'


    def test_click_on_button_question_of_order_cancel(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_order_cancel)
        important_on_page.click_on_button(Locators.button_question_of_order_cancel)
        important_on_page.wait_for_load_text(Locators.text_for_order_cancel)
        element = important_on_page.get_text(Locators.text_for_order_cancel)
        assert element == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'


    def test_click_on_button_question_of_order_outside_mkad(self):
        important_on_page = ImportantQuestionsPage(self.driver)

        important_on_page.go_to_questions()
        important_on_page.wait_for_load_title(Locators.button_question_of_order_outside_mkad)
        important_on_page.click_on_button(Locators.button_question_of_order_outside_mkad)
        important_on_page.wait_for_load_text(Locators.text_for_order_outside_mkad)
        element = important_on_page.get_text(Locators.text_for_order_outside_mkad)
        assert element == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()