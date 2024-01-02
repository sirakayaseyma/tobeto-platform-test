import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


class Test_calendar:
  
  def tobeto_giris(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/")
    self.driver.maximize_window() 
  
  #Eğitim ve Etkinlik Takvimine giriş
  def test_calendar_login(self):
    self.tobeto_giris()
    calendar = WebDriverWait(self.driver,6).until(ec.visibility_of_element_located((By.CLASS_NAME, "calendar-btn")))
    calendar.click()
    sleep(3)
  
  #Eğitim ve Etkinlik Takviminden çıkış 
  def test_calendar_out(self):
    self.test_calendar_login()
    sleep(3)
    calendar_out = WebDriverWait(self.driver,6).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/button")))
    calendar_out.click()
    sleep(3)
    
    


  
