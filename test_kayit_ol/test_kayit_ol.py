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

class Test_kayit_ol:
    
        def  giris_ekrani(self):
            self.driver = webdriver.Chrome()
            self.driver.get(gc.URL)
            self.driver.maximize_window() 
    
        def test_basarili_kayit(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Şeyma")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("seymasirakaya@gmail.com")
                password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
                password.send_keys("123456")
                passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
                passwordAgain.send_keys("123456")
                registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
                registerbutton.click()
                InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
                InputAcikRizaMetni.click()
                Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
                Inputuyeliksoz.click()
                Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
                Inputemailonay.click()
                Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
                Inputphoneonay.click()
                phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
                phoneNumber.send_keys("5355551123") 
                iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
                self.driver.switch_to.frame(iframe)
                sleep(1)
                captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
                captcha.click()
                sleep(10)
                self.driver.switch_to.default_content()
                sleep(3)
                continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
                continueButton.click()
                sleep(3)

        
        def test_gecersiz_eposta(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Şeyma")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("a?.4")
                sleep(3)
               
                
        def test_onkarakter_tel(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Şeyma")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("seymasirakaya@gmail.com")
                password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
                password.send_keys("abc123")
                passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
                passwordAgain.send_keys("abc123")
                registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
                registerbutton.click()
                InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
                InputAcikRizaMetni.click()
                Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
                Inputuyeliksoz.click()
                Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
                Inputemailonay.click()
                Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
                Inputphoneonay.click()
                phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
                phoneNumber.send_keys("53555")
                sleep(2)
                iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
                self.driver.switch_to.frame(iframe)
                sleep(1)
                captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
                captcha.click()
                sleep(35)
                self.driver.switch_to.default_content()
                sleep(3)
                continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
                continueButton.click()
                sleep(3) 
                errorMessage = self.driver.find_element(By.XPATH ,"/html/body/div[4]/div/div/div/div/div/label[4]/small/p")
                telnoHata = errorMessage.text == "En az 10 karakter girmelisiniz."
                print(f"Telefon No Mesaji: {telnoHata}")
               
                
        def test_kayitli_eposta(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Şeyma")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("sirakaya.seymaa@gmail.com")
                password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
                password.send_keys("111111")
                passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
                passwordAgain.send_keys("111111")
                registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
                registerbutton.click()
                InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
                InputAcikRizaMetni.click()
                Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
                Inputuyeliksoz.click()
                Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
                Inputemailonay.click()
                Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
                Inputphoneonay.click()
                phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
                phoneNumber.send_keys("5355551123") 
                iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
                self.driver.switch_to.frame(iframe)
                sleep(1)
                captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
                captcha.click()
                sleep(8)
                self.driver.switch_to.default_content()
                sleep(3)
                continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
                continueButton.click()
                sleep(3) 
                errorKayit = self.driver.find_element(By.CLASS_NAME , "toast-body")
                kayitliPostaHata = errorKayit.text == "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."
                print(f"Kayitli E-posta Hatasi: {kayitliPostaHata}")
                sleep(6)
        
        def test_sifre_alti_az(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Osman")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("srkyosman@gmail.com")
                password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
                password.send_keys("1234")
                passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
                passwordAgain.send_keys("1234")
                registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
                registerbutton.click()
                InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
                InputAcikRizaMetni.click()
                Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
                Inputuyeliksoz.click()
                Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
                Inputemailonay.click()
                Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
                Inputphoneonay.click()
                phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
                phoneNumber.send_keys("5355551123") 
                iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
                self.driver.switch_to.frame(iframe)
                sleep(1)
                captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
                captcha.click()
                sleep(12)
                self.driver.switch_to.default_content()
                sleep(3)
                continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
                continueButton.click()
                sleep(3) 
                errorSifre = self.driver.find_element(By.CLASS_NAME,"toast-body")
                sifreHata = errorSifre.text == "• Şifreniz en az 6 karakterden oluşmalıdır."
                print(f"6 Karakter Hatası: {sifreHata}")
                sleep(6)
                
        def test_sifre_eslesmedi(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Osman")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("osmansirakayaa1@gmail.com")
                password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
                password.send_keys("1234567")
                passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
                passwordAgain.send_keys("123498")
                registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
                registerbutton.click()
                InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
                InputAcikRizaMetni.click()
                Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
                Inputuyeliksoz.click()
                Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
                Inputemailonay.click()
                Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
                Inputphoneonay.click()
                phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
                phoneNumber.send_keys("5355551123") 
                iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
                self.driver.switch_to.frame(iframe)
                sleep(1)
                captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
                captcha.click()
                sleep(12)
                self.driver.switch_to.default_content()
                sleep(3)
                continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
                continueButton.click()
                sleep(3) 
                errorSifre = self.driver.find_element(By.CLASS_NAME,"toast-body")
                sifreEslesmemeHata = errorSifre.text == "• Şifreler eşleşmedi"
                print(f"Şifre Eşleşmeme Hatası: {sifreEslesmemeHata}")
                sleep(6)
        
        def test_two_error(self):
                self.giris_ekrani()
                name = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.NAME)))
                name.send_keys("Şeyma")
                surname = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.SURNAME)))
                surname.send_keys("Sirakaya")
                email = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL)))
                email.send_keys("sirakaya.seymaa@gmail.com")
                password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PASSWORD)))
                password.send_keys("1234")
                passwordAgain = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.PSW_AGAIN)))
                passwordAgain.send_keys("1234")
                registerbutton = self.driver.find_element(By.XPATH, gc.REGISTER_BTN)
                registerbutton.click()
                InputAcikRizaMetni = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ACIK_RIZA)))
                InputAcikRizaMetni.click()
                Inputuyeliksoz = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.UYELIK)))
                Inputuyeliksoz.click()
                Inputemailonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.EMAIL_CLICK)))
                Inputemailonay.click()
                Inputphoneonay = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, gc.ARAMA_CLICK)))
                Inputphoneonay.click()
                phoneNumber = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME, gc.PHONE)))
                phoneNumber.send_keys("5355551123") 
                iframe=self.driver.find_element(By.XPATH, gc.IFRAME )
                self.driver.switch_to.frame(iframe)
                sleep(1)
                captcha=self.driver.find_element(By.XPATH,gc.CAPTCHA)
                captcha.click()
                sleep(40)
                self.driver.switch_to.default_content()
                sleep(3)
                continueButton = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.XPATH, gc.CONTINUE_BUTTON)))
                continueButton.click()
                sleep(3) 
                twoError = self.driver.find_element(By.CLASS_NAME , "toast-body")
                Errorstwo = twoError.text == "• 2 errors occurred"
                print(f"Kayitli e-posta ve 6 karakterden az: {Errorstwo}")
                sleep(6)
        
            
           
        
        

        