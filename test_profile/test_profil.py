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

class Test_profil:   
        

        def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://tobeto.com/giris")
            self.driver.maximize_window() 
            
        def basarili_giris(self):
            self.giris_ekrani()
            email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, gc.NAME_TAG)))
            email.send_keys("seymaagundogduuu@gmail.com")
            sleep(3)
            psw = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_TAG)))
            psw.send_keys("tobeto_test")
            loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
            loginbutton.click()
            sleep(4)
            
        def profil_bilgilerim(self):
            self.basarili_giris()
          
            buton_tiklama = self.driver.find_element(By.XPATH, gc.BUTON_TIKLAMA)
            buton_tiklama.click()
            sleep(2)
            profil_tiklama = self.driver.find_element(By.XPATH, gc.PROFIL_TIKLAMA)
            profil_tiklama.click()
            sleep(4)
        
        def test_bilgiler_doldur(self):
            self.profil_bilgilerim()
          
            name = self.driver.find_element(By.NAME, gc.NAME)
            name.send_keys("")
            surname = self.driver.find_element(By.NAME, gc.SURNAME)
            surname.send_keys("")
            tel_no = self.driver.find_element(By.XPATH, gc.TEL_NO)
            tel_no.send_keys("")
            sleep(3)
            birthday_input = self.driver.find_element(By.NAME, "birthday")

            # Doğum tarihi gönder
            birthday_input.send_keys("19-07-1999")  
            ## self.driver.execute_script('arguments[0].value = "2023-09-21";', birtday)
            sleep(3)
            identifier =self.driver.find_element(By.NAME, gc.IDENTIFIER)
            identifier.send_keys("")
            sleep(3)
            country = self.driver.find_element(By.NAME, gc.COUNTRY)
            country.send_keys("")
            sleep(4)
            city = self.driver.find_element(By.NAME, gc.CITY)
            city.click()
            cityName = self.driver.find_element(By.XPATH, gc.CITY_NAME)
            cityName.click()
            sleep(3)
            district = self.driver.find_element(By.NAME, gc.DISTRICT)
            district.click()
            districtName = self.driver.find_element(By.XPATH, gc.DISTRICT_NAME)
            districtName.click()
            sleep(3)
            address = self.driver.find_element(By.NAME, gc.ADDRESS)
            address.send_keys("Misket 60 Cadde 5 No:4")
            sleep(2)
            
            description =self.driver.find_element(By.XPATH, gc.DESCRIPTION)
            description.send_keys("Kendimi geliştiriyorum, yazılım testi yapmak en büyük hobim")
            sleep(3)
            saveBtn = self.driver.find_element(By.XPATH, gc.SAVE_BTN )
            saveBtn.click()
            sleep(3)
            sonuc = self.driver.find_element(By.CLASS_NAME , "toast-body")
            sonuc1 = sonuc.text == "• Bilgileriniz başarıyla güncellendi."
            print(f"Bilgiler Güncellendi {sonuc1}")
            sleep(6)
        
        def test_bilgiler_bos(self):
            self.profil_bilgilerim()
            saveBtn = self.driver.find_element(By.XPATH, gc.SAVE_BTN )
            saveBtn.click()
            sleep(3)  
            
            
            

