#import time
#import math
#import sys
import pytest
from selenium import webdriver

from test_main_page import browser
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import unittest

class BasePage():
    def __init__(self, browser, url): #создание конструктора - метода, который первым запускается каждый раз при создании объекта
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url) #не забываем про self! Это говорит программе о том, что обращаться нужно к свойствам созданного объекта