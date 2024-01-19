from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gc


class Test_egitimler:   
        def giris_ekrani(self):
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
            psw.send_keys("*****")
            loginbutton = self.driver.find_element(By.XPATH, gc.GIRIS_YAP_XPATH)
            loginbutton.click()
            sleep(2)
            self.driver.execute_script("window.scrollBy(0, 500);")    # Aşağıya 200 piksel kaydırma
            sleep(2)
        
        def test_egitim(self):
            self.test_basarili_giris()
            egitimlerim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.LESSONS)))
            egitimlerim.click()
            sleep(3)
            dfg = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.DFG)))
            dfg.click()
            sleep(3)
         #eğitim ismiyle eşleşen veri konrolü
            search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.SEARCH)))
            search_btn.send_keys("h")
            sleep(5)
        #eğitim arama butonun içini silme
            search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.SEARCH)))
            search_btn.clear()
            sleep(5)
        #eğitim olmayan arama yapma 
            search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.SEARCH)))
            search_btn.send_keys("w")
            sleep(5)
            metin = WebDriverWait(self.driver,4).until(ec.visibility_of_element_located((By.XPATH, gc.EGITIM)))
            testResult = metin.text == "Size atanan herhangi bir eğitim bulunmamaktadır."
            print(f"Eğitim yok sonucu: {testResult}")
            sleep(3)
         #sayfa yenilenir
            self.driver.get("https://tobeto.com/egitimlerim")
            self.driver.refresh()
            sleep(5)
         #kurum seçimi arama butonu İstanbul Kodluyor seçimi
            kurum_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.KURUM)))
            kurum_btn.click()
            istkod = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, gc.IST)))
            istkod.click()            
            sleep(3)
            self.driver.get("https://tobeto.com/egitimlerim")
            self.driver.refresh()
            sleep(5)
      
        
        #Devam ettiklerim
            devam_ettiklerim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.DEVAM)))
            devam_ettiklerim.click() 
            sleep(3) 
        #tumegitimler
            tumegitim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TUM)))
            tumegitim.click() 
            sleep(3)
          #Tamamladıklarım
            tamamladiklarim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TAMAMLA)))
            tamamladiklarim.click() 
            sleep(3)
         # eğitime git 
            egitimegit = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.EGITIMGIT)))
            egitimegit.click()
            sleep(5)
          
       
