from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestChatbot:
    def test_chatbot_icon(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window() 

        try:
            # Sayfanın tamamen yüklenmesini bekleyin
            WebDriverWait(self.driver, 10).until(EC.title_contains("Expected Page Title"))

            # Chatbot ikonunu bulmak için bekleyin
            chatbot_icon = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='launcher']/div/img")))
            
            # Chatbot ikonuna tıkla
            chatbot_icon.click()
            sleep(5)

        except Exception as e:
            print(f"Hata oluştu: {e}")

        finally:
            # Tarayıcıyı kapatın
            self.driver.quit()


test_class = TestChatbot()
test_class.test_chatbot_icon()
