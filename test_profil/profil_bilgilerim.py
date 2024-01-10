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

class test_profil:   
        

        def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://tobeto.com/giris")
            self.driver.maximize_window() 
            
        def test_basarili_giris(self):
            self.giris_ekrani()
            email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, gc.NAME_TAG)))
            email.send_keys("seymaagundogduuu@gmail.com")
            sleep(3)
            psw = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_TAG)))
            psw.send_keys("tobeto_test")
            loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
            loginbutton.click()
            sleep(4)
            
        def test_profil_bilgilerim(self):
            self.test_basarili_giris()
          
            buton_tiklama = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")
            buton_tiklama.click()
            sleep(2)
            profil_tiklama = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")
            profil_tiklama.click()
            sleep(4)
        
        def test_bilgiler_doldur(self):
            self.test_profil_bilgilerim()
            sleep(3)
            #birtday = self.driver.find_element(By.NAME, "birtday")
            #self.driver.execute_script('arguments[0].value = "2023-09-21";', birtday)
            # sleep(3)
            identifier =self.driver.find_element(By.NAME, "identifier")
            identifier.send_keys("41296946900")
            sleep(3)
            country = self.driver.find_element(By.NAME, "country")
            country.send_keys("TÜRKİYE")
            sleep(4)
            city = self.driver.find_element(By.NAME, "city")
            city.click()
            cityName = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select/option[8]")
            cityName.click()
            sleep(3)
            district = self.driver.find_element(By.NAME, "district")
            district.click()
            districtName = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select/option[20]")
            districtName.click()
            sleep(3)
            address = self.driver.find_element(By.NAME, "address")
            address.send_keys("Misket 60 Cadde 5 No:4")
            sleep(2)
            
            description =self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea")
            description.send_keys("Kendimi geliştiriyorum, yazılım testi yapmak en büyük hobim")
            sleep(3)
            saveBtn = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button")
            saveBtn.click()
            sleep(3)
            
            
            

test = test_profil()
test.test_bilgiler_doldur()