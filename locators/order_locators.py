from selenium.webdriver.common.by import By

class Locators:
    button_order_main = (By.CLASS_NAME, 'Button_Button__ra12g') # Кнопка "Заказать" сверху на главной странице
    button_order_lower_part = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]") # Кнопка "Заказать" снизу на главной странице
    button_order = (By.XPATH, ".//div[contains(@class, 'Order_Button')]/button[contains(text(), 'Заказать')]") # Кнопка "Заказать" на странице заказа
    name_field = (By.XPATH, ".//input[@placeholder='* Имя']") # Поле "Имя"
    last_name_field = (By.XPATH, ".//input[@placeholder='* Фамилия']") # Поле "Фамилия"
    address_field = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']") # Поле "Адрес"
    metro_station_field = (By.CLASS_NAME, 'select-search__input') # Поле "Станция Метро"
    metro_station_value = (By.XPATH, ".//div[@class='select-search__select']/ul/li[4]") # Выбор значения станции метро
    phone_field = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']") # Поле "Номер телефона"
    button_next = (By.XPATH, ".//button[text()='Далее']") # Кнопка "Далее"
    when_to_bring_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") # Поле "Выбор даты доставки"
    when_to_bring_value = (By.XPATH, ".//div[contains(@class,'react-datepicker__day--021')]") # Выбор значения даты доставки
    period_field = (By.XPATH, ".//div[@class='Dropdown-placeholder']") # Поле "Период"
    period_field_value = (By.XPATH, ".//div[text()='трое суток']") # Выбор периода
    color_scooter_field = (By.XPATH, ".//input[@id='black']/parent::label") # Поле "Цвет"
    comments_field = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") # Поле "Комментарии"
    button_yes = (By.XPATH, ".//div[contains(@class, 'Order_Button')]/button[contains(text(), 'Да')]") # Кнопка "Да"
    status_order = (By.XPATH, ".//div[(@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен')]") # Текст статуса заказа
    logo_scooter = [By.XPATH, ".//img[@alt='Scooter']"] # Логотип "Самоката"
    logo_yandex = [By.XPATH, ".//img[@alt='Yandex']"] # Логотип "Яндекса"
    text_info_about_scooter = [By.CLASS_NAME, "Home_SubHeader__zwi_E"] # Информация о самокатах на главной странице



