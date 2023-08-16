from selenium.webdriver.common.by import By

class Locators:
    important_questions = [By.CLASS_NAME, "Home_SubHeader__zwi_E"]

    button_question_of_cost = [By.ID, 'accordion__heading-0']
    button_question_of_multiple_scooters = [By.ID, 'accordion__heading-1']
    button_question_of_rental_time = [By.ID, 'accordion__heading-2']
    button_question_of_order_for_today = [By.ID, 'accordion__heading-3']
    button_question_of_order_extension = [By.ID, 'accordion__heading-4']
    button_question_of_charging = [By.ID, 'accordion__heading-5']
    button_question_of_order_cancel = [By.ID, 'accordion__heading-6']
    button_question_of_order_outside_mkad = [By.ID, 'accordion__heading-7']

    text_for_cost = [By.XPATH, ".//p[contains(text(),'Сутки — 400 рублей')]"]
    text_for_multiple_scooters = [By.XPATH, ".//p[contains(text(),'один самокат')]"]
    text_for_rental_time = [By.XPATH, ".//p[contains(text(),'оформляете заказ')]"]
    text_for_order_for_today = [By.XPATH, ".//p[contains(text(),'завтрашнего дня')]"]
    text_for_order_extension = [By.XPATH, ".//p[contains(text(),'поддержку')]"]
    text_for_charging = [By.XPATH, ".//p[contains(text(),'заряд')]"]
    text_for_order_cancel = [By.XPATH, ".//p[contains(text(),'Штрафа')]"]
    text_for_order_outside_mkad = [By.XPATH, ".//p[contains(text(),'Москв')]"]




