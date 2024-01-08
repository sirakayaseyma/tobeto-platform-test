## Test Senaryo Adı: Chatbot kontrolü yapılacaktır.
#### Açıklama: Kullanıcının chatbot sistemini test etmek için oluşturulmuştur.
#### Ön Koşul: Kullanıcı https://tobeto.com/giris web sitesine erişmiş olmalıdır.
## Test Case 1: Yeni mesaj bölümü kontrolü
#### Adımlar:
#### 1. Chatbot butonuna tıklayın.
#### Beklenen sonuç:Ekranda açılır pencere şeklinde yeni bir mesaj bölümü açılmalıdır.

![Alt text](images/chatbotikonu.png)

![Alt text](images/mesajyazma.png)

### Test Case 2: Mesaj bölümü kapama kontrolü
#### Ön Koşul: Mesaj bölümü açık olmalıdır.
#### Adımlar:
#### 1. Simge durumuna getir ikonuna tıklayın.
#### Beklenen Sonuç: Mesaj bölümü kapanmalıdır.

![Alt text](images/simgekucultme.png)

## Test Case 3: Uyarı Mesajı Kontrolü
#### Ön Koşul: Mesaj bölümü açık olmalıdır.
#### Adımlar:
#### 1. Mesajlaşmayı bitirme ikonuna tıklayın.
#### Beklenen Sonuç: Ekranda “Görüşmeyi bitirmek istediğinize emin misiniz?” Uyarı mesajı gözlenmelidir.

![Alt text](images/mesajbitirme.png)

## Test Case 4: Puanlama Tablosu Kontrolü
#### Ön Koşul: Mesajlaşmayı bitirme ikonuna tıklanmış olmalıdır.
#### Adımlar:
#### 1) Görüşmeyi bitirmek istediğinize emin misiniz? Uyarı mesajında “Evet” butonuna tıklayın.
#### Beklenen Sonuç:Ekranda görüşme hakkında geri bildirim almak için mesaj ekranına puanlama tablosu gelmelidir.


## Chatbot Açma Kapama Pytest Kontrolü
![Alt text](images/acmakapamapytest.png)