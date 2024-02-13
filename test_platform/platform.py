from pathlib import Path
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

class Test_platform:   
        def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://tobeto.com/giris")
            self.driver.maximize_window() 
        
        def tearDown(self):
            self.driver.quit()
 
        def test_basarili_giris(self):
            self.giris_ekrani()
            email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, gc.NAME_TAG)))
            email.send_keys("sirakaya.seymaa@gmail.com")
            sleep(2)
            psw = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_TAG)))
            psw.send_keys("******")
            loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
            loginbutton.click()
            sleep(2)
            self.driver.execute_script("window.scrollBy(0, 500);")    # Aşağıya 200 piksel kaydırma
            sleep(2)
        
        def test_platform(self):
            self.test_basarili_giris()
            #Eğitimlerim kontrolü
            egitimlerim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.LESSONS)))
            egitimlerim.click()
            sleep(3)
            
            #Duyuru ve haber kontrolü
            duyuruvehaber = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.NOTIFICATION)))
            duyuruvehaber.click()
            sleep(3)

            #Anketlerim kontrolü
            anket = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.SURVEY)))
            anket.click()
            sleep(3)
            
            #Basvuru kontrolü
            basvuru = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.APPLY)))
            basvuru.click()
            sleep(3)
            
testClass = Test_platform()
testClass.test_platform()