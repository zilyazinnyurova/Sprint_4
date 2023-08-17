from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import Locators
from selenium.webdriver.support.select import Select


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def clic_on_button_order_top(self):
        self.driver.find_element(*Locators.button_order_top).click()

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

    def wait_for_load_station(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.metro_station_value))

    def set_metro_station(self):
        clickable_el = self.driver.find_element(*Locators.metro_station_value)
        self.driver.execute_script("arguments[0].click();", clickable_el)



    # Номер
    def clic_on_phone_field(self):
        self.driver.find_element(*Locators.phone_field).click()

    def set_phone(self, phone_field):
        self.driver.find_element(*Locators.phone_field).send_keys(phone_field)