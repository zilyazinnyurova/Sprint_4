from selenium.webdriver.common.by import By

class Locators:
    button_order_top = [By.CLASS_NAME, 'Button_Button__ra12g']
    button_order = [By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM']
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    last_name_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]

    metro_station_value = [By.XPATH, ".//div[(text()='Красносельская')]"]

    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
