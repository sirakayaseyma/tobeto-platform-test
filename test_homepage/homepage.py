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


class test_tobetocom:
    
    def tobeto(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://tobeto.com/")
            self.driver.maximize_window() 
    
        
    def test_homepage(self):
        self.tobeto()
        whoarewe = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.WHOAREWE)))
        whoarewe.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/hakkimizda":
            print("WHO ARE YOU URL true")
        else:
            print("WHO ARE YOU URL false")
        sleep(3)
        
        tobeto = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TOBETO)))
        tobeto.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/":
            print("TOBETO URL true")
        else:
            print("TOBETO URL false")
        sleep(3)
        
        # what do we offer => forindividuals , forinstitutions
        whatdoweoffer = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.WHATDOWEOFFER)))
        whatdoweoffer.click()
        sleep(2)
        woforindividuals = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FORINDIVIDUALS)))
        woforindividuals.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/bireyler-icin":
            print("FOR INDIVIDUALS URL true")
        else:
            print("FOR INDIVIDUALS URL false")
        sleep(3)
        
        whatdoweoffer = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,gc.WHATDOWEOFFER)))
        whatdoweoffer.click()
        sleep(2)
        woforinstitutions = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FORINSTITUTIONS)))
        woforinstitutions.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/kurumlar-icin":
            print("FOR INSTITUTIONS URL true")
        else:
            print("FOR INSTITUTIONS URL false")
        sleep(3)
        
        catalog= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CATALOG)))
        catalog.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/katalog":
            print("CATALOG URL true")
        else:
            print("CATALOG URL false")
        sleep(3)
        
        codecademy= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CODECADEMY)))
        codecademy.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/codecademy":
            print("CODECADEMY URL true")
        else:
            print("CODECADEMY URL false")
        sleep(3)
        
        # Login Button
        
        
        login = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.LOGIN))) 
        login.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/giris":
            print("LOGIN URL true")
        else:
            print("LOGIN URL false")
        sleep(3)
        
        # sign up for free
        signup = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.SIGNUP))) 
        signup.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/kayit-ol":
            print("SIGN UP URL true")
        else:
            print("SIGN UP URL false")
        sleep(3)
        
        #Apply Button 
        apply = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.APPLY))) 
        apply.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/istanbul-kodluyor":
            print("APPLY URL true")
        else:
            print("APPLY URL false")
        sleep(3)
        
        # turn back 
        self.driver.back()
        
        #Tobeto this month
        tbtthismonth = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TBTTISMONTH)))
        tbtthismonth.click()
        sleep(2)
        blog= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.BLOG)))
        blog.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/blog":
            print("BLOG URL true")
        else:
            print("BLOG URL false")
        sleep(3)
        
        tbtthismonth = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TBTTISMONTH)))
        tbtthismonth.click()
        sleep(2)
        weareinthepress = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.WEAREINTHEPRESS)))
        weareinthepress.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/basinda-biz":
            print("INTHEPRESS URL true")
        else:
            print("INTHEPRESS  URL false")
        sleep(3)
        
        tbtthismonth = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TBTTISMONTH)))
        tbtthismonth.click()
        sleep(2)
        calendar = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CALENDAR)))
        calendar.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/basinda-biz":
            print("CALENDAR URL true")
        else:
            print("CALENDAR  URL false")
        sleep(3)
        
        tbtthismonth = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.TBTTISMONTH)))
        tbtthismonth.click()
        sleep(2)
        istanbulcoding = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.ISTANBULCODING)))
        istanbulcoding.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/istanbul-kodluyor":
            print("İSTANBUL CODING URL true")
        else:
            print("İSTANBUL CODING  URL false")
        sleep(3)
        
        
test_home = test_tobetocom()
test_home.test_homepage()