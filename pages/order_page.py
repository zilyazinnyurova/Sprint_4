from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def clic_on_button_cookie(self):
        self.driver.find_element(*Locators.button_cookie).click()

    def wait_for_load(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element_locator), message=f'Not found {element_locator}')

    def clic_on_button_order_main(self):
        self.driver.find_element(*Locators.button_order_top).click()

    def clic_on_button_order(self):
        self.driver.find_element(*Locators.button_order_lower_part).click()
    # Имя
    def clic_on_name_field(self):
        self.driver.find_element(*Locators.name_field).click()

    def set_name(self, name):
        self.driver.find_element(*Locators.name_field).send_keys(name)

    # Фамилия
    def clic_on_last_name_field(self):
        self.driver.find_element(*Locators.last_name_field).click()

    def set_last_name(self, last_name):
        self.driver.find_element(*Locators.last_name_field).send_keys(last_name)

    # Адрес
    def clic_on_address_field(self):
        self.driver.find_element(*Locators.address_field).click()

    def set_address(self, adress):
        self.driver.find_element(*Locators.address_field).send_keys(adress)

    # Станция
    def clic_on_metro_station_field(self):
        self.driver.find_element(*Locators.metro_station_field).click()

    def set_metro_station(self):
        selectbox_el = self.driver.find_element(*Locators.metro_station_field)
        for i in range(4):
            selectbox_el.send_keys(Keys.DOWN)
        selectbox_el.send_keys(Keys.ENTER)

    # Номер
    def clic_on_phone_field(self):
        self.driver.find_element(*Locators.phone_field).click()

    def set_phone(self, phone_field):
        self.driver.find_element(*Locators.phone_field).send_keys(phone_field)

    def clic_on_button_next(self):
        clickable_el = self.driver.find_element(*Locators.button_next)
        self.driver.execute_script("arguments[0].click();", clickable_el)

# ПРО АРЕНДУ
    def clic_on_when_to_bring_field(self):
        self.driver.find_element(*Locators.when_to_bring_field).click()
    def set_when_to_bring_value(self):
        self.driver.find_element(*Locators.when_to_bring_value).click()

    def clic_on_period_field(self):
        self.driver.find_element(*Locators.period_field).click()
    def set_period_field_value(self):
        self.driver.find_element(*Locators.period_field_value).click()

    def clic_on_color_scooter_field(self):
        self.driver.find_element(*Locators.color_scooter_field).click()

    def clic_on_comments_field(self):
        self.driver.find_element(*Locators.comments_field).click()

    def set_comments_field_value(self, comments):
        self.driver.find_element(*Locators.comments_field).send_keys(comments)

    def clic_on_button_yes(self):
        self.driver.find_element(*Locators.button_yes).click()

    # LOGO
    def clic_on_logo_scooter(self):
        self.driver.find_element(*Locators.logo_scooter).click()

    def clic_on_logo_yandex(self):
        self.driver.find_element(*Locators.logo_yandex).click()

    def get_text(self, element_locator):
        return self.driver.find_element(*element_locator).text

    def go_to_button_lower_part(self):
        element = self.driver.find_element(*Locators.button_order_lower_part)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)