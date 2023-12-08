#from conftest import browser
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла


from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Нет кнопки 'добавить в корзину'"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def captcha(self):
        #basket_link = self.browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket') 
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET) 
        self.browser.implicitly_wait(5)

        basket_link.click()
        self.solve_quiz_and_get_code()

    


    