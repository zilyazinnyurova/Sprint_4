from selenium.webdriver.common.by import By

class Locators:
    important_questions = [By.CLASS_NAME, "Home_SubHeader__zwi_E"] # Текст "Важные вопросы"

    button_question_of_cost = [By.ID, 'accordion__heading-0'] # Кнопка "Важные вопросы:стоимость"
    button_question_of_multiple_scooters = [By.ID, 'accordion__heading-1'] # Кнопка "Важные вопросы:несколько самокатов"
    button_question_of_rental_time = [By.ID, 'accordion__heading-2'] # Кнопка "Важные вопросы:время аренды"
    button_question_of_order_for_today = [By.ID, 'accordion__heading-3'] # Кнопка "Важные вопросы:заказ на сегодня"
    button_question_of_order_extension = [By.ID, 'accordion__heading-4'] # Кнопка "Важные вопросы:продление"
    button_question_of_charging = [By.ID, 'accordion__heading-5'] # Кнопка "Важные вопросы:зарядка"
    button_question_of_order_cancel = [By.ID, 'accordion__heading-6'] # Кнопка "Важные вопросы:отмена"
    button_question_of_order_outside_mkad = [By.ID, 'accordion__heading-7'] # Кнопка "Важные вопросы:доставка за МКАД"

    text_for_cost = [By.XPATH, ".//p[contains(text(),'Сутки — 400 рублей')]"] # Ответ на "Важные вопросы:стоимость"
    text_for_multiple_scooters = [By.XPATH, ".//p[contains(text(),'один самокат')]"] # Ответ на "Важные вопросы:несколько самокатов"
    text_for_rental_time = [By.XPATH, ".//p[contains(text(),'оформляете заказ')]"] # Ответ на "Важные вопросы:время аренды"
    text_for_order_for_today = [By.XPATH, ".//p[contains(text(),'завтрашнего дня')]"] # Ответ на "Важные вопросы:заказ на сегодня"
    text_for_order_extension = [By.XPATH, ".//p[contains(text(),'поддержку')]"] # Ответ на "Важные вопросы:продление"
    text_for_charging = [By.XPATH, ".//p[contains(text(),'заряд')]"] # Ответ на "Важные вопросы:зарядка"
    text_for_order_cancel = [By.XPATH, ".//p[contains(text(),'Штрафа')]"] # Ответ на "Важные вопросы:отмена"
    text_for_order_outside_mkad = [By.XPATH, ".//p[contains(text(),'Москв')]"] # Ответ на "Важные вопросы:доставка за МКАД"




