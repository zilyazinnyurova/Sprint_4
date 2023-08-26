from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    @allure.step("Открыть браузер и сайт по ссылке https://qa-scooter.praktikum-services.ru/")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, element_locator):
        self.driver.find_element(*element_locator).click()

    @allure.step("Кликнуть на некликабельный элемент")
    def click_on_unclickable_element(self, element_locator):
        clickable_el = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].click();", clickable_el)

    @allure.step("Ожидает наличие элемента на странице")
    def wait_visibility_of_element(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element_locator),
                                             message=f'Not found {element_locator}')

    @allure.step("Проверяет, что элемент есть на странице и его видно")
    def wait_presence_of_element(self, element_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element_locator),
                                             message=f'Not found {element_locator}')

    @allure.step('Скролить до конкретного элемента страницы')
    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение текста')
    def get_text(self, element_locator):
        return self.driver.find_element(*element_locator).text

    @allure.step('Вводим значение в поле')
    def set_value_for_field(self, element_locator, value):
        self.driver.find_element(*element_locator).send_keys(value)

    @allure.step('Проверяем ссылку в адресной строке')
    def check_url_match(self, url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_matches(url))


    @allure.step('Ожидаем количество табов в браузере')
    def wait_n_tabs(self, n):
        return WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(n))