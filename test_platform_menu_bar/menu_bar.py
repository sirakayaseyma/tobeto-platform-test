from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gc
import pytest
from selenium.webdriver.common.alert import Alert

class test_menu_bar:   
        def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://tobeto.com/giris")
            self.driver.maximize_window() 
        
        def login(self):
            self.giris_ekrani()
            email = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME, gc.NAME_TAG)))
            email.send_keys("seymaagundogduuu@gmail.com")
            sleep(2)
            psw = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME, gc.PSW_TAG)))
            psw.send_keys("tobeto_test")
            loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
            loginbutton.click()
            sleep(2)
        
        def test_menu_bar_ikon(self):
            self.login()
            profilimBtn = self.driver.find_element(By.XPATH, gc.PROFILIM)
            profilimBtn.click()
            sleep(3)
            degerlendirmeBtn = self.driver.find_element(By.XPATH, gc.DEGERLENDIRMELER)
            degerlendirmeBtn.click()
            sleep(3)
            katalogBtn = self.driver.find_element(By.XPATH, gc.KATALOG)
            katalogBtn.click()
            sleep(3)
            takvimBtn = self.driver.find_element(By.XPATH, gc.TAKVIM)
            takvimBtn.click()
            sleep(3)
            anasayfaBtn = self.driver.find_element(By.XPATH, gc.ANASAYFA)
            anasayfaBtn.click()
            sleep(2)
            istKodBtn = self.driver.find_element(By.XPATH, gc.ISTANBUL_KODLUYOR)
            istKodBtn.click()
            sleep(3)
            #istanbulkodluyor ekranında sayfa sonlanır.
            
        #Sol üst menüde yer alan Tobeto ikonu kontrolü , burada anasayfaya yönlendirme yapar.
        def test_tobeto_ikon(self):
            self.login()
            profilimBtn = self.driver.find_element(By.XPATH, gc.PROFILIM)
            profilimBtn.click()
            sleep(3)
            degerlendirmeBtn = self.driver.find_element(By.XPATH, gc.DEGERLENDIRMELER)
            degerlendirmeBtn.click()
            sleep(3)
            katalogBtn = self.driver.find_element(By.XPATH, gc.KATALOG)
            katalogBtn.click()
            sleep(3)
            takvimBtn = self.driver.find_element(By.XPATH, gc.TAKVIM)
            takvimBtn.click()
            sleep(3)
            tobetoUstBtn = self.driver.find_element(By.XPATH, gc.TOBETO_SOL_IKON)
            tobetoUstBtn.click()
            sleep(13)
            
            
    
            
            

testClass = test_menu_bar()
testClass.test_menu_bar_ikon()
testClass.test_tobeto_ikon()

            