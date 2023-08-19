from selenium.webdriver.common.by import By


class Locators:
    button_order_top = [By.CLASS_NAME, 'Button_Button__ra12g']

    button_order = [By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM']
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    last_name_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]

    metro_station_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_station_value = [By.XPATH, ".//div/div[2]/ul/li[4]/button/div[2][(text()='Сокольники')]"]

    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = (By.XPATH, ".//button[text()='Далее']")

    when_to_bring_field = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    when_to_bring_value = []

    period_field = []
    period_field_value = []

    color_scooter_field = [By.XPATH, ".//input[@id='black']/parent::label"]

    comments_field = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    button_yes = [By.XPATH, ".//button[text()='Да']"]
    status_order = [By.XPATH, ".//div[text()='Заказ оформлен']"]


    # LOGO
    logo_scooter = [By.XPATH, ".//img[@alt='Scooter']"]
    logo_yandex = [By.XPATH, ".//img[@alt='Yandex']"]
    important_questions = [By.CLASS_NAME, "Home_SubHeader__zwi_E"]

