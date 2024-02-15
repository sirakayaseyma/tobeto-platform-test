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


class test_communication:
    
    def tobeto(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/iletisim")
        self.driver.maximize_window() 
    
    def communication_success(self):
        self.tobeto()
        element_locator = (By.XPATH, gc.NAMESURNAME)
        namesurname = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(element_locator))
        namesurname.send_keys("Şeyma Sırakaya")
        sleep(2)
        element_locator2 = (By.XPATH, gc.EMAIL)
        email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(element_locator2))
        email.send_keys("sirakaya.seymaa@gmail.com")
        sleep(2)
        element_locator3 = (By.XPATH, gc.MESSAGE)
        message = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(element_locator3))
        message.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s")
        sleep(2)
        
        # Sayfanın yüksekliğini al
        page_height = self.driver.execute_script("return document.body.scrollHeight")

        scroll_position = page_height / 2 - 200  # Sayfanın yarısından 200 piksel yukarı
        self.driver.execute_script("window.scrollTo(0, {});".format(scroll_position))

        # Scroll işleminin tamamlanması için bekleyin
        sleep(3)
        
        iframe = self.driver.find_element(By.XPATH, gc.IFRAME )
        self.driver.switch_to.frame(iframe)
        sleep(3)
        
        element_locator4 = (By.XPATH, gc.RECAPTCHA_CLICK)
        recaptcha = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located(element_locator4))
        recaptcha.click()
        
        sleep(2)
        # iframeden çık
        self.driver.switch_to.default_content()
        sleep(3)
        send =  WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, gc.SEND)))
        send.click()
        sleep(4)
        
        message = self.driver.find_element(By.CLASS_NAME , "toast-body")
        message2= message.text == "• Mesajınız gönderildi..."
        print(f"İletişim Mesajı {message2}")
        sleep(6)  

testproject = test_communication()
testproject.communication_success()
        