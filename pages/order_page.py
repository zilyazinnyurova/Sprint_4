from locators.order_locators import Locators
from selenium.webdriver.common.keys import Keys
from base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Кликаем на лого Самокат')
    def click_logo_scooter(self):
        self.click_on_unclickable_element(Locators.logo_scooter)

    @allure.step('Кликаем на лого Яндекс')
    def click_logo_yandex(self):
        self.click_on_element(Locators.logo_yandex)

    @allure.step('Кликаем на кнопку "Заказать" в верхней части страницы')
    def click_header_order_button(self):
        self.click_on_element(Locators.button_order_main)

    @allure.step('Кликаем на кнопку "Заказать" в нижней части страницы')
    def click_footer_order_button(self):
        self.click_on_unclickable_element(Locators.button_order_lower_part)

    @allure.step('Переходим на следующую страницу заказа')
    def move_to_next_page_of_order(self):
        self.click_on_unclickable_element(Locators.button_next)

    @allure.step('Клик на кнопку размещения заказа')
    def click_place_order_button(self):
        self.scroll_to_element(Locators.button_order)
        self.click_on_unclickable_element(Locators.button_order)

    @allure.step('Клик на кнопку подтверждения заказа')
    def click_confirm_order_button(self):
        self.click_on_element(Locators.button_yes)

    @allure.step('Получения текста статуса заказа')
    def get_order_status_text(self):
        return self.get_text(Locators.status_order)


    @allure.step('Заполняем поля на первой странице заказа')
    def fill_first_page_of_order(self, user_data):
        self.click_on_element(Locators.name_field)
        self.set_value_for_field(Locators.name_field, user_data['name'])
        self.click_on_element(Locators.last_name_field)
        self.set_value_for_field(Locators.last_name_field, user_data['last_name'])
        self.click_on_element(Locators.address_field)
        self.set_value_for_field(Locators.address_field, user_data['address'])
        self.click_on_element(Locators.metro_station_field)
        self.wait_visibility_of_element(Locators.metro_station_field)
        self.set_metro_station()
        self.click_on_element(Locators.phone_field)
        self.set_value_for_field(Locators.phone_field, user_data['phone'])

    @allure.step('Заполняем поля на второй странице заказа')
    def fill_second_page_of_order(self, user_data):
        self.click_on_element(Locators.when_to_bring_field)
        self.click_on_element(Locators.when_to_bring_value)
        self.click_on_element(Locators.period_field)
        self.click_on_element(Locators.period_field_value)
        self.click_on_element(Locators.color_scooter_field)
        self.click_on_element(Locators.comments_field)
        self.set_value_for_field(Locators.comments_field, user_data['comment'])

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self):
        selectbox_el = self.driver.find_element(*Locators.metro_station_field)
        for i in range(4):
            selectbox_el.send_keys(Keys.DOWN)
        selectbox_el.send_keys(Keys.ENTER)
