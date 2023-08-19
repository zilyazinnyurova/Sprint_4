from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage
from locators.order_locators import Locators
from selenium.webdriver.support.ui import Select



class TestPraktikumScooter:
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    def test_click_on_button_order(self):
        order_page = OrderPage(self.driver)

        order_page.clic_on_button_order_top()

        order_page.clic_on_name_field()
        order_page.set_name('Зиля')

        order_page.clic_on_last_name_field()
        order_page.set_last_name('Зиннюрова')

        order_page.clic_on_address_field()
        order_page.set_address('Сокольническая площадь д.9')

        # order_page.clic_on_metro_station_field()
        order_page.set_metro_station()
        # order_page.wait_for_load_station(Locators.metro_station_field)

        order_page.clic_on_phone_field()
        order_page.set_phone('89372826434')

        order_page.clic_on_button_next()

        order_page.clic_on_when_to_bring_field()
        order_page.set_when_to_bring_value()

        order_page.clic_on_period_field()
        order_page.set_period_field_value()

        order_page.clic_on_color_scooter_field()
        order_page.set_color_scooter_value()

        order_page.clic_on_comments_field()
        order_page.set_comments_field_value('test')

        order_page.clic_on_button_yes()

        element = order_page.wait_for_load(Locators.status_order)
        assert element == 'Заказ оформлен'


    def test_click_on_logo_scooter(self):
        order_page = OrderPage(self.driver)

        order_page.clic_on_button_order_top()
        order_page.clic_on_logo_scooter()
        element = order_page.wait_for_load(Locators.important_questions)
        assert element == 'Вопросы о важном'

    def test_click_on_logo_ya(self):
        order_page = OrderPage(self.driver)

        order_page.clic_on_logo_yandex()
        element = order_page.wait_for_load(Locators.important_questions)
        assert element == 'Вопросы о важном'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()