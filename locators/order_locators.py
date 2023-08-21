from selenium.webdriver.common.by import By


class Locators:

    button_cookie = (By.CLASS_NAME, 'App_CookieButton__3cvqF')

    button_order_top = (By.CLASS_NAME, 'Button_Button__ra12g')
    button_order_lower_part = (By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать')]")


    name_field = (By.XPATH, ".//input[@placeholder='* Имя']")
    last_name_field = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_field = (By.CLASS_NAME, 'select-search__input')
    metro_station_value = (By.XPATH, ".//div[@class='select-search__select']/ul/li[4]")
    phone_field = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, ".//button[text()='Далее']")
    when_to_bring_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    when_to_bring_value = (By.XPATH, ".//div[contains(@class,'react-datepicker__day--021')]")
    period_field = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    period_field_value = (By.XPATH, ".//div[text()='трое суток']")
    color_scooter_field = (By.XPATH, ".//input[@id='black']/parent::label")
    comments_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']")

    # button_yes = (By.XPATH, ".//button[contains(@class,'Button_Button__ra12g')]")
    button_yes = (By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да')]")
    status_order = (By.XPATH, ".//div[(@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен')]")


    # LOGO
    logo_scooter = [By.XPATH, ".//img[@alt='Scooter']"]
    logo_yandex = [By.XPATH, ".//img[@alt='Yandex']"]
    text_info_about_scooter = [By.CLASS_NAME, "Home_SubHeader__zwi_E"]

    # ОШИБКИ В ПОЛЯХ
    error_text_for_metro_station_field = [By.XPATH, ".//div[text()='Выберите станцию']"]


