from selenium.common.exceptions import NoSuchElementException
#from test_main_page import browser
class BasePage():
    def __init__(self, browser, url, timeout=10): #создание конструктора - метода, который первым запускается каждый раз при создании объекта
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) #Используем неявное ожидание, т.е. не говорим интерпретатору, какой именно объект мы ждем.
    
    def open(self):
        self.browser.get(self.url) #не забываем про self! Это говорит программе о том, что обращаться нужно к свойствам созданного объекта
    
    def is_element_present(self, how, what): #перехватываем исключения
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException): #Если исключение найдено, то возвращаем false, иначе true
            return False
        return True