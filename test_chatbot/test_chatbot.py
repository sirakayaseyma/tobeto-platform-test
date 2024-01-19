from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test_Chatbot:
    def giris(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window() 
    
    def test_chatbot_icon_open(self):
    
        self.giris()
        wait = WebDriverWait(self.driver, 10)   # Maksimum bekleme süresi (saniye cinsinden)
        
        # İframe geçişini beklemek için implicit veya explicit bekleme kullanabilirsiniz.
        iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-launcher-frame")))
        self.driver.switch_to.frame(iframe)

        # İçeriklerin yüklenmesini beklemek için explicit bekleme kullanabilirsiniz.
        launcher_button = wait.until(EC.element_to_be_clickable((By.ID, "launcher")))
        launcher_button.click()
        sleep(5)
        
        
        
    def test_chatbot_icon_close(self):
        self.test_chatbot_icon_open()
        self.driver.switch_to.default_content()
        wait = WebDriverWait(self.driver, 20)

        iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-conversation-frame")))
        self.driver.switch_to.frame(iframe)

        # SVG elemanını bekleyerek bul
        svg_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @class='exw-minimize-button header-button']")))
        svg_element.click()

        sleep(5)  # Bekleme süresini ihtiyacınıza göre ayarlayabilirsiniz.


    def test_uyari_mesaj(self):
        self.test_chatbot_icon_open()
        self.driver.switch_to.default_content()
        wait = WebDriverWait(self.driver, 20)

        iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-conversation-frame")))
        self.driver.switch_to.frame(iframe)

        # SVG2 elemanını bekleyerek bul
        svg_element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @class='exw-end-session-button header-button']")))
        svg_element2.click()

        sleep(5)  # Bekleme süresini ihtiyacınıza göre ayarlayabilirsiniz.
        
        #EVET Butonuna Tıklama 
        # yes_Btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='exw-conversation-frame-body']/div/div/div/div[1]/div/div[3]/div/button[1]")))
        # yes_Btn.click()
        # sleep(3)

        
        #HAYIR Butonuna Tıklama 
        # no_Btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='exw-conversation-frame-body']/div/div/div/div[1]/div/div[3]/div/button[2]")))
        # no_Btn.click()
        # sleep(3)
        
    def test_evet_gorus(self):
        self.test_chatbot_icon_open()
        self.driver.switch_to.default_content()
        wait = WebDriverWait(self.driver, 20)

        iframe = wait.until(EC.presence_of_element_located((By.ID, "exw-conversation-frame")))
        self.driver.switch_to.frame(iframe)

        # SVG2 elemanını bekleyerek bul
        svg_element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @class='exw-end-session-button header-button']")))
        svg_element2.click()

        sleep(5)  # Bekleme süresini ihtiyacınıza göre ayarlayabilirsiniz.
        
        #EVET Butonuna Tıklama 
        yes_Btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='exw-conversation-frame-body']/div/div/div/div[1]/div/div[3]/div/button[1]")))
        yes_Btn.click()
        sleep(10)
        
        gorus_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='surveyTextArea']")))
        gorus_input.send_keys("TOBETO harika bir platform")
        sleep(10)
        
        gndr_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='surveyForm']//*[@id='surveyBtn']")))
        self.driver.execute_script("arguments[0].click();", gndr_btn)
       
        
        message = self.driver.find_element(By.XPATH, "//*[@id='exw-messages']/div[2]/div/div/div/h3")
        gorusmesaji =  message.text == "Geri bildiriminiz için teşekkürler!"
        print(f"Görüş Bildirimi : {gorusmesaji}")
        
        
        sleep(5)
        
        
    
    
                
         
             
