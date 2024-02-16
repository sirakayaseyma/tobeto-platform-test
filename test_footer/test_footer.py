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

class Test_footer:
    
    def page(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com")
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
 
        
    def test_sitemap(self):
        self.page()
        sleep(5)
        
        aboutus = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.ABOUT_US)))
        aboutus.click()
        sleep(5)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/hakkimizda":
            print("About Us true")
        else:
            print("About Us false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        
        for_individuals = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FOR_INDIVUDUALS)))
        for_individuals.click()
        sleep(5)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/bireyler-icin":
            print("For individuals true")
        else:
            print("For individuals false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
                
        for_institutions = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FOR_INSTITUTIONS)))
        for_institutions.click()
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/kurumlar-icin":
            print("For institutions true")
        else:
            print("For institutions false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        
        corporate_identity = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CORPORATE_IDENTITY)))
        corporate_identity.click()
        sleep(5)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/kurumsal-kimlik":
            print("Corporate Identity true")
        else:
            print("Corporate Identity false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        
        faq = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FAQ)))
        faq.click()
        sleep(5)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/sss":
            print("FAQ true")
        else:
            print("FAQ false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        
        communication = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.COMMUNICATION)))
        communication.click()
        sleep(5)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/iletisim":
            print("Communication true")
        else:
            print("Communication false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
    
    def test_resources(self):
        self.page()
        
        membership_agreement = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.MEMBERSHIP)))
        membership_agreement.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        kvkk = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.KVKK)))
        kvkk.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        related_person = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.RELATED_PERSON)))
        related_person.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        cookie_policy = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.COOKIE_POLICY)))
        cookie_policy.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        withdrawal_form =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.WITHDRAWAL_FORM)))
        withdrawal_form.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        
    def test_educational_journeys(self):
        self.page()
        sleep(3)
        
        front_end = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FRONTEND)))
        front_end.click()
        sleep(2)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/programlar/frontend":
            print("Frontend true")
        else:
            print("Frontend false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        full_stack = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.FULL_STACK)))
        full_stack.click()
        sleep(2)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/programlar/full-stack-developer":
            print("Full Stack true")
        else:
            print("Full Stack false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        web_mobile = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.WEB_MOBILE)))
        web_mobile.click()
        sleep(2)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/programlar/web-mobile":
            print("Web & Mobile true")
        else:
            print("Web & Mobile false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        data_science = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.DATA_SCIENCE)))
        data_science.click()
        sleep(2)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/yakinda":
            print("Data Science true")
        else:
            print("Data Science false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        cyber_security =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.CYBER_SECURITY)))
        cyber_security.click()
        sleep(2)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/yakinda":
            print("Cyber Security true")
        else:
            print("Cyber Security false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        
        ux_ui =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, gc.UX_UI)))
        ux_ui.click()
        sleep(2)
        current_url = self.driver.current_url
        if current_url == "https://tobeto.com/yakinda":
            print("UX UI true")
        else:
            print("UX UI false")
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)