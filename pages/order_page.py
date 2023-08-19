from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import Locators
from selenium.webdriver.support.ui import Select
import time



class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element_locator)).text

    def clic_on_button_order_top(self):
        self.driver.find_element(*Locators.button_order_top).click()

    def clic_on_button_order(self):
        self.driver.find_element(*Locators.button_order).click()
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
        clickable_el = self.driver.find_element(*Locators.metro_station_value).click()
        self.driver.execute_script("arguments[0].click();", clickable_el)

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
        self.driver.find_element(*Locators.when_to_bring_value).send_keys()

    def clic_on_period_field(self):
        self.driver.find_element(*Locators.period_field).click()
    def set_period_field_value(self):
        self.driver.find_element(*Locators.period_field_value).send_keys()

    def clic_on_color_scooter_field(self):
        self.driver.find_element(*Locators.color_scooter_field).click()
    def set_color_scooter_value(self):
        self.driver.find_element(*Locators.color_scooter_field).send_keys()

    def clic_on_comments_field(self):
        self.driver.find_element(*Locators.color_scooter_field).click()
    def set_comments_field_value(self, comments):
        self.driver.find_element(*Locators.color_scooter_field).send_keys(comments)

    def clic_on_button_yes(self):
        self.driver.find_element(*Locators.button_yes).click()

    # LOGO
    def clic_on_logo_scooter(self):
        self.driver.find_element(*Locators.logo_scooter).click()

    def clic_on_logo_yandex(self):
        self.driver.find_element(*Locators.logo_yandex).click()
