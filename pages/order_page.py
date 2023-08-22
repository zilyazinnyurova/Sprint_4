from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage:

    @allure.step("Открыть браузер и сайт по ссылке https://qa-scooter.praktikum-services.ru/")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждать пока не появится элемент")
    def wait_for_load(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element_locator), message=f'Not found {element_locator}')

    @allure.step("Кликаем на кнопку 'Заказать сверху'")
    def clic_on_button_order_main(self):
        self.driver.find_element(*Locators.button_order_main).click()

    def clic_on_button_order(self):
        clickable_el = self.driver.find_element(*Locators.button_order_lower_part)
        self.driver.execute_script("arguments[0].click();", clickable_el)

    @allure.step('Кликаем на поле "Имя"')
    def clic_on_name_field(self):
        self.driver.find_element(*Locators.name_field).click()

    @allure.step('Вводим значение в поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(*Locators.name_field).send_keys(name)

    @allure.step('Кликаем на поле "Фамилия"')
    def clic_on_last_name_field(self):
        self.driver.find_element(*Locators.last_name_field).click()
    @allure.step('Вводим значение в поле "Фамилия"')
    def set_last_name(self, last_name):
        self.driver.find_element(*Locators.last_name_field).send_keys(last_name)

    @allure.step('Кликаем на поле "Адрес"')
    def clic_on_address_field(self):
        self.driver.find_element(*Locators.address_field).click()

    @allure.step('Вводим значение в поле "Адрес"')
    def set_address(self, adress):
        self.driver.find_element(*Locators.address_field).send_keys(adress)

    @allure.step('Кликаем на поле "Станция метро"')
    def clic_on_metro_station_field(self):
        self.driver.find_element(*Locators.metro_station_field).click()

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self):
        selectbox_el = self.driver.find_element(*Locators.metro_station_field)
        for i in range(4):
            selectbox_el.send_keys(Keys.DOWN)
        selectbox_el.send_keys(Keys.ENTER)

    @allure.step('Кликаем на поле "Номер"')
    def clic_on_phone_field(self):
        self.driver.find_element(*Locators.phone_field).click()

    @allure.step('Вводим значение в поле "Номер"')
    def set_phone(self, phone_field):
        self.driver.find_element(*Locators.phone_field).send_keys(phone_field)

    @allure.step("Кликаем на кнопку 'Далее'")
    def clic_on_button_next(self):
        clickable_el = self.driver.find_element(*Locators.button_next)
        self.driver.execute_script("arguments[0].click();", clickable_el)

    @allure.step('Кликаем на поле "Когда привезти заказ"')
    def clic_on_when_to_bring_field(self):
        self.driver.find_element(*Locators.when_to_bring_field).click()

    @allure.step('Выбираем дату в календаре для "Когда привезти заказ"')
    def set_when_to_bring_value(self):
        self.driver.find_element(*Locators.when_to_bring_value).click()

    @allure.step('Кликаем на поле "Срок аренды"')
    def clic_on_period_field(self):
        self.driver.find_element(*Locators.period_field).click()

    @allure.step('Выбираем значение для строки "Срок аренды"')
    def set_period_field_value(self):
        self.driver.find_element(*Locators.period_field_value).click()

    @allure.step('Кликаем на цвет самоката')
    def clic_on_color_scooter_field(self):
        self.driver.find_element(*Locators.color_scooter_field).click()

    @allure.step('Кликаем на поле "Комментарии"')
    def clic_on_comments_field(self):
        self.driver.find_element(*Locators.comments_field).click()

    @allure.step('Вводим значение в поле "Комментарии"')
    def set_comments_field_value(self, comments):
        self.driver.find_element(*Locators.comments_field).send_keys(comments)

    @allure.step('Кликаем на кнопку "Да"')
    def clic_on_button_yes(self):
        self.driver.find_element(*Locators.button_yes).click()

    @allure.step('Кликаем на логотип "Самокат"')
    def clic_on_logo_scooter(self):
        clickable_el = self.driver.find_element(*Locators.logo_scooter)
        self.driver.execute_script("arguments[0].click();", clickable_el)

    @allure.step('Кликаем на логотип "Яндекс"')
    def clic_on_logo_yandex(self):
        self.driver.find_element(*Locators.logo_yandex).click()

    @allure.step('Получить текст"')
    def get_text(self, element_locator):
        return self.driver.find_element(*element_locator).text

    @allure.step('Скролить до кнопки "Заказать" в нижний части страницы')
    def go_to_button_lower_part(self):
        element = self.driver.find_element(*Locators.button_order_lower_part)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

