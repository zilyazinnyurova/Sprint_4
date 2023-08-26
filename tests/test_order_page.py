from pages.order_page import OrderPage
from locators.order_locators import Locators
from data.urls import Urls
import pytest
import allure


class TestPraktikumScooter:
    @allure.description("tc-1.Оформление заказа через кнопку расположенную сверху.")
    @pytest.mark.parametrize('user_data', [
        {
            'last_name': 'Зиннюрова',
            'name': 'Зиля',
            'address': 'Сокольническая площадь д.9',
            'phone': '79274960169',
            'comment': 'test'
        },
        {
            'last_name': 'Иванов',
            'name': 'Иван',
            'address': 'Большая Лубянка д.150',
            'phone': '89196976726',
            'comment': 'Привезти нужно до пол 5, иначе нет нужды.Позвоните перед приездом.'
        }])
    def test_click_on_button_order_main(self, driver, user_data):
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        order_page.click_footer_order_button()
        order_page.fill_first_page_of_order(user_data)
        order_page.move_to_next_page_of_order()
        order_page.fill_second_page_of_order(user_data)
        order_page.click_place_order_button()
        order_page.click_confirm_order_button()
        status = order_page.get_order_status_text()
        assert status.startswith('Заказ оформлен')

    @allure.description("tc-2.Переход на форму заказа через кнопку расположенную снизу.")
    def test_click_on_button_lower_part(self, driver):
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        order_page.click_footer_order_button()
        assert order_page.check_url_match(Urls.order_page)

    @allure.description("tc-3.Проверка кликабельности логотипа 'Самокат' и перехода на нужный адрес.")
    def test_click_on_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.click_logo_scooter()
        order_page.click_header_order_button()
        order_page.click_logo_scooter()
        scooter_info = order_page.get_text(Locators.text_info_about_scooter)
        assert scooter_info == 'Привезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

    @allure.description("tc-4.Проверка кликабельности логотипа 'Яндекс' и перехода на нужный адрес.")
    def test_click_on_logo_ya(self, driver):
        original_window = driver.current_window_handle

        order_page = OrderPage(driver)
        order_page.click_logo_yandex()
        order_page.wait_n_tabs(2)

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        assert order_page.check_url_match(Urls.dzen_page)
