from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage
from locators.order_locators import Locators
import pytest
import allure


class TestPraktikumScooter:
    @allure.step('Открываем браузер Firefox и сайт')
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.description("tc-1.Оформление заказа через кнопку расположенную сверху.")
    @pytest.mark.parametrize('user_data', [{'last_name': 'Зиннюрова', 'name': 'Зиля', 'address': 'Сокольническая площадь д.9', 'phone': '79274960169', 'comment': 'test'}, {'last_name': 'Иванов', 'name': 'Иван', 'address': 'Большая Лубянка д.150', 'phone': '89196976726', 'comment': 'Привезти нужно до пол 5, иначе нет нужды.Позвоните перед приездом.'}])
    def test_click_on_button_order_main(self, user_data):
        order_page = OrderPage(self.driver)
        order_page.clic_on_logo_scooter()

        @allure.step('Кликаем на кнопку "Заказать сверху')
        order_page.clic_on_button_order_main()
        @allure.step('Кликаем на поле "Имя" и вводим значение')
        order_page.clic_on_name_field()
        order_page.set_name(user_data['name'])
        @allure.step('Кликаем на поле "Фамилия" и вводим значение')
        order_page.clic_on_last_name_field()
        order_page.set_last_name(user_data['last_name'])
        @allure.step('Кликаем на поле "Адрес" и вводим значение')
        order_page.clic_on_address_field()
        order_page.set_address(user_data['address'])
        @allure.step('Кликаем на поле "Станция метро" и выбираем значение')
        order_page.clic_on_metro_station_field()
        order_page.wait_for_load(Locators.metro_station_field)
        order_page.set_metro_station()
        @allure.step('Кликаем на поле "Номер" и вводим значение')
        order_page.clic_on_phone_field()
        order_page.set_phone(user_data['phone'])
        @allure.step('Кликаем на кнопку "Далее"')
        order_page.clic_on_button_next()
        @allure.step('Кликаем на поле "Когда привезти" и выбираем дату')
        order_page.clic_on_when_to_bring_field()
        order_page.set_when_to_bring_value()
        @allure.step('Кликаем на поле "Срок аренды" и выбираем значение')
        order_page.clic_on_period_field()
        order_page.set_period_field_value()
        @allure.step('Кликаем на чекбокс')
        order_page.clic_on_color_scooter_field()
        @allure.step('Кликаем на поле "Комментарии" и вводим значение')
        order_page.clic_on_comments_field()
        order_page.set_comments_field_value(user_data['comment'])
        @allure.step('Скролим и кликаем на кнопку "Заказать"')
        order_page.go_to_button_lower_part()
        order_page.clic_on_button_order()
        @allure.step('Кликаем на кнопку "Да"')
        order_page.clic_on_button_yes()

        element = order_page.get_text(Locators.status_order)
        assert element.startswith('Заказ оформлен')

    @allure.description("tc-2.Переход на форму заказа через кнопку расположенную снизу.")
    def test_click_on_button_lower_part(self):
        order_page = OrderPage(self.driver)
        order_page.clic_on_logo_scooter()
        order_page.clic_on_button_order()
        assert WebDriverWait(self.driver, 10).until(expected_conditions.url_matches('https://qa-scooter.praktikum-services.ru/order'))

    @allure.description("tc-3.Проверка кликабельности логотипа 'Самокат' и перехода на нужный адрес.")
    def test_click_on_logo_scooter(self):
        order_page = OrderPage(self.driver)
        order_page.clic_on_logo_scooter()
        order_page.clic_on_button_order_main()
        order_page.clic_on_logo_scooter()
        element = order_page.get_text(Locators.text_info_about_scooter)
        assert element == 'Привезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

    @allure.description("tc-4.Проверка кликабельности логотипа 'Яндекс' и перехода на нужный адрес.")
    def test_click_on_logo_ya(self):
        original_window = self.driver.current_window_handle

        order_page = OrderPage(self.driver)
        order_page.clic_on_logo_yandex()

        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        assert WebDriverWait(self.driver, 10).until(expected_conditions.url_matches('https://dzen.ru'))

    @allure.step('Закрываем браузер')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()