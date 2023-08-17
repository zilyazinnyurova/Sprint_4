from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage
from locators.order_locators import Locators
from selenium.webdriver.support.select import Select



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


        order_page.clic_on_metro_station_field()
        # order_page.wait_for_load_station()
        order_page.set_metro_station()


        order_page.clic_on_phone_field()
        order_page.set_phone('89372826434')

        # element = order_page.get_text(Locators.text_for_cost)
        # assert element == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()