#import time
#import math
#import sys
#import pytest
#from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import unittest
from .base_page import BasePage #импортируем базовый класс из указанного файла

class MainPage(BasePage): #Таким образом этот класс будет иметь доступ ко всем методам своего класса-родителя
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) #* обозначает, что нам необходимо раскрыть кортеж 
        login_link.click()
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" #Если ошибка не обнаружена, то отрабатывает код дозапятой
        #Иначе - после запятой
