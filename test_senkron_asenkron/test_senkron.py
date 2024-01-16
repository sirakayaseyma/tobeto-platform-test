from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gc
import pytest
from selenium.webdriver.common.alert import Alert

class Test_senkron:   
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
            
        def test_senkron_login(self):
            self.login()
            egitimlerim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.LESSONS)))
            egitimlerim.click()
            sleep(3)
            dfg = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.DFG)))
            dfg.click()
            sleep(3)
            senkron = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.SENKRON)))
            senkron.click()
            sleep(10)
        
        #begen butonu kotnrolü
        def test_senkron_begen(self):
            self.test_senkron_login()
            ikon_like = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.IKON_LIKE)))
            ikon_like.click()
            sleep(3)
        
        #begenen kisileri görüntüleme
        def test_begen_kisi(self):
            self.test_senkron_login()
            person = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PERSON)))
            person.click()
            sleep(3)
        def test_aboutcontentrecord(self):
            self.test_senkron_login()
            #hakkında alanına tıklayın
            about = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.ABOUT)))
            about.click()
            sleep(5)
            #içerik alanına tıklayın
            content = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CONTENT)))
            content.click()
            sleep(5)
            #Kaydı aç alanına tıklayın
            record = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.RECORD)))
            record.click()
            sleep(5)
        
        def test_work(self):
            self.test_senkron_login()
            work = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.WORK)))
            work.click()
            sleep(5)
            
        def test_work_detail(self):
            self.test_work()
            sleep(10)
            work_detail = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.WORK_DETAIL)))
            work_detail.click()
            sleep(5)
            