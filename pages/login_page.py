from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        #self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_url_consist('login'), "Не нашли login в адресной строке браузера"
        
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SING_IN), "Кнопки войти нет" 
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SING_UP), "Нет кнопки регистрации" 
#        assert True
    