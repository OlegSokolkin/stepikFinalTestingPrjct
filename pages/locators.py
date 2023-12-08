from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #обращаем внимание, что в классе мы жестко указываем несколько значений 

class LoginPageLocators():
    SING_IN = (By.XPATH, '//button[@name="login_submit"]')
    SING_UP = (By.XPATH, '//button[@name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')