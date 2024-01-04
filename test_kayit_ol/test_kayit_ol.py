from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gc
import openpyxl
import pytest
from selenium.webdriver.common.alert import Alert

class test_kayit_ol:
    
    def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get(gc.URL)
            self.driver.maximize_window() 
    
    def test_basarili_kayit(self):
        self.giris_ekrani()
        name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
        name.send_keys("Şeyma")
        surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
        surname.send_keys("Sirakaya")
        email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
        email.send_keys("seymasirakaya@gmail.com")
        password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
        password.send_keys("abc123")
        passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
        passwordAgain.send_keys("abc123")
        registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
        registerbutton.click()
        InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
        InputAcikRizaMetni.click()
        Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
        Inputuyeliksoz.click()
        Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
        Inputemailonay.click()
        Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
        Inputphoneonay.click()
        phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
        phoneNumber.send_keys("5355551123") 
        iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
        self.driver.switch_to.frame(iframe)
        sleep(1)
        captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
        captcha.click()
        sleep(1)
        self.driver.switch_to.default_content()
        sleep(3)
        continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
        continueButton.click()
        sleep(3)
           
        
        
testClass = test_kayit_ol()
testClass.test_basarili_kayit()
        