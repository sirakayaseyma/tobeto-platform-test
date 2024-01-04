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


class test_sifre_sifirlama:
    def  giris_ekrani(self):
        self.driver = webdriver.Chrome()
        self.driver.get(gc.PLATFORM_GIRIS_URL)
        self.driver.maximize_window() 
    
    def test_kayitli_hesap_sifirlama(self):
        self.giris_ekrani()
        
        #Şifre sıfırlama ekranına giden butona bas 
        sifirlaBtn = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.SIFIRLA_BTN)))
        sifirlaBtn.click()
        
        #Kayıtlı kullanıcı için e-mail adresi gir 
        email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.EMAIL_BOX)))
        email.send_keys("sirakaya.seymaa@gmail.com")
        sleep(2)
        
        #Gönder butonu 
        gndrBtn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.GNDR_BTN)))
        gndrBtn.click()
        sleep(4)
        
        #mesaj
        assertMessage = self.driver.find_element(By.CLASS_NAME, "toast-body")
        result1 =  assertMessage.text == "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
        print(f"Test Sonucu: {result1}")
    
    def test_kayitli_olmayan_hesap_sifirlama(self):
        self.giris_ekrani()
        
        #Şifre sıfırlama ekranına giden butona bas 
        sifirlaBtn = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.SIFIRLA_BTN)))
        sifirlaBtn.click()
        
        #Kayıtlı kullanıcı için e-mail adresi gir 
        email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.EMAIL_BOX)))
        email.send_keys("111@gmail.com")
        sleep(2)
        
        #Gönder butonu 
        gndrBtn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.GNDR_BTN)))
        gndrBtn.click()
        sleep(4)
        
        #mesaj
        assertMessage = self.driver.find_element(By.CLASS_NAME, "toast-body")
        result2 =  assertMessage.text == "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
        print(f"Test Sonucu: {result2}")
        
    def test_gecersiz_email_sifirlama(self):
        self.giris_ekrani()
        
        #Şifre sıfırlama ekranına giden butona bas 
        sifirlaBtn = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.SIFIRLA_BTN)))
        sifirlaBtn.click()
        
        #Email formatına uygun olmayan bir şeyler gir 
        email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.EMAIL_BOX)))
        email.send_keys("gmail123")
        sleep(2)
        
        #Gönder butonu 
        gndrBtn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.GNDR_BTN)))
        gndrBtn.click()
        sleep(4)
        
        #Hata mesajı 
        assertMessage = self.driver.find_element(By.CLASS_NAME, "toast-body")
        result =  assertMessage.text == "• Girdiğiniz e-posta geçersizdir."
        print(f"Test Sonucu: {result}")
        
testClass = test_sifre_sifirlama()
testClass.test_kayitli_hesap_sifirlama()
testClass.test_kayitli_olmayan_hesap_sifirlama()
testClass.test_gecersiz_email_sifirlama()

        