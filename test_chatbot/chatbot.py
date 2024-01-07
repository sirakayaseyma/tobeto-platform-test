from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class test_Chatbot:
    def giris(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window() 
    
    # İkonun açılabilmesini sorgulamak için kullanılır.
    def test_chatbot_icon(self):
        self.giris()
        wait = WebDriverWait(self.driver, 15)   # Maksimum bekleme süresi (saniye cinsinden)
        
        # İframe geçişini beklemek için implicit veya explicit bekleme kullanabilirsiniz.
        iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-launcher-frame")))
        self.driver.switch_to.frame(iframe)

        # İçeriklerin yüklenmesini beklemek için explicit bekleme kullanabilirsiniz.
        launcher_button = wait.until(EC.element_to_be_clickable((By.ID, "launcher")))
        launcher_button.click()
        sleep(10)
                   
    def test_chatbot_kapama(self):
            self.test_chatbot_icon()
            sleep(5)
        
        # CSS selektörü kullanarak SVG öğesini bulma
            svg_element = self.driver.find_element(By.XPATH, "//*[@id='exw-conversation-frame-body']/div/div/div/div[1]/div/div[2]/svg[1]")

        # SVG üzerinde tıklama
            if svg_element:
                svg_element.click()

            # WebDriver'ı kapatma
            self.driver.quit()
                    
         
             
test_class = test_Chatbot()
test_class.test_chatbot_icon()
#test_class.test_chatbot_kapama()
