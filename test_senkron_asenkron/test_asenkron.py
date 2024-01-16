from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gc
import pytest
from selenium.webdriver.common.alert import Alert

class Test_asenkron:   
        def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://tobeto.com/giris")
            self.driver.maximize_window() 
        
        def login(self):
            self.giris_ekrani()
            email = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME, gc.NAME_TAG)))
            email.send_keys("sirakaya.seymaa@gmail.com")
            sleep(2)
            psw = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME, gc.PSW_TAG)))
            psw.send_keys("****")
            loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
            loginbutton.click()
            sleep(2)
        
        def test_asenkron_login(self):
            self.login()
            egitimlerim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.LESSONS)))
            egitimlerim.click()
            sleep(3)
            dfg = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.DFG)))
            dfg.click()
            sleep(3)
            asenkron = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.SOFTSKILL)))
            asenkron.click()
            sleep(10)
        
        #begen butonu kotnrolü , buton beğenilmediyse
        def test_asenkron_begen(self):
            self.test_asenkron_login()
            ikon_like = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.IKON_LIKE)))
            ikon_like.click()
            sleep(3)
        
        #begen butonu kontrolü , buton beğenildiyse
        def test_asenkron_begen_gerial(self):
            self.test_asenkron_login()
            ikon_dislike = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.IKON_DISLIKE)))
            ikon_dislike.click()
            sleep(3)
        
        #begenen kisileri görüntüleme
        def test_begen_kisi(self):
            self.test_asenkron_login()
            person = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PERSON)))
            person.click()
            sleep(3)
        
        def test_aboutcontent(self):
            self.test_asenkron_login()
            #hakkında alanına tıklayın
            about = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.ABOUT)))
            about.click()
            sleep(5)
            #içerik alanına tıklayın
            content = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CONTENT)))
            content.click()
            sleep(5)