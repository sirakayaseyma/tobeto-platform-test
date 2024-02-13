from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from constants import globalConstants as gc
from time import sleep
import pytest
from selenium.webdriver.common.alert import Alert

class Test_signout:
    def giris(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window() 
        
    def login(self):
        self.giris()
        email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, gc.NAME_TAG)))
        email.send_keys("sirakaya.seymaa@gmail.com")
        sleep(3)
        psw = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_TAG)))
        psw.send_keys("*****")
        loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
        loginbutton.click()
        sleep(5)

    def test_logout(self):
        self.login()
        profile = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.PROFILE )))
        profile.click()
        sleep(2)
        logout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.LOGOUT)))
        logout.click()
        sleep(3)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/giris":
            print("URL true")
        else:
            print("URL false")
        sleep(3)