from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.important_questions_locators import Locators

class ImportantQuestionsPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_questions(self):
        element = self.driver.find_element(*Locators.important_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_load_title(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element_locator))

    def click_on_button(self, element_locator):
        clickable_el = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].click();", clickable_el)

    def wait_for_load_text(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element_locator))

    def get_text(self, element_locator):
        return self.driver.find_element(*element_locator).text
