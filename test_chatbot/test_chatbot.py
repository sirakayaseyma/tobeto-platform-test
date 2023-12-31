from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
#from constants import globalConstants as gc
import openpyxl
import pytest
from selenium.webdriver.common.alert import Alert

class test_chatbot:
    def test_chatbot_ikon(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window() 
        chatbotIkon = WebDriverWait(self.driver,6).until(ec.visibility_of_element_located((By.CLASS_NAME, "frame-content")))
        chatbotIkon.click()
        sleep(5)
        
testClass = test_chatbot()
testClass.test_chatbot_ikon()