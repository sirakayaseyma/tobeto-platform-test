## Test Senaryosu: Kullanıcının web sitesinde bulunan üst menü barda yer alan içeriklerin görüntülenmesi kontrol edilecektir.
#### Açıklama: Kullanıcının web sitesinde bulunan sayfa başlıklarını görüntülemesi ve sayfada gezilebilmesi test etmesi için oluşturulmuştur.
#### Ön Koşul: https://tobeto.com/platform web sitesine erişilmiş olmalıdır. Test edilebilir kullanıcı hesabına giriş yapılmış olmalıdır.

## Test Case 1: TOBETO üst menüsündeki öğelere tıklama test edilecektir.
#### Adımlar:
#### 1. https://tobeto.com/platform sayfasına girin.
#### 2. "Değerlendirmeler" yazısına tıklayın.
####    Beklenen Sonuç: Kullanıcı Değerlendirmeler sayfasına yönlendirilmelidir.

![Alt text](images/degerlendirmeler.png)

#### 3."Profilim" yazısına tıklayın.
####    Beklenen Sonuç: Kullanıcı Profil sayfasına yönlendirilmelidir.

![Alt text](images/profilim.png)

#### 4. "Katalog" yazısına tıklayın.
####    Beklenen Sonuç: Kullanıcı Katalog sayfasına yönlendirilmelidir.

![Alt text](images/katalog.png)

#### 5. "Takvim" yazısına tıklayın.
####    Beklenen Sonuç: Kullanıcı Takvim sayfasına yönlendirilmelidir.

![Alt text](images/takvim.png)

#### 6. "Anasayfa" yazısına tıklayın.
#### Beklenen Sonuç: Kullanıcı Ana sayfaya yönlendirilir.

![Alt text](images/anasayfa.png)

#### 7. En altta yer alan "Tobeto" yazısına tıklayın.
####    Beklenen Sonuç: Kullanıcı "https://tobeto.com/" sayfasına yönlendirilmelidir.

![Alt text](images/tobetocom.png)

##### Beklenen Sonuç: Kullanıcı tüm sayfalara yönlendirilmeli ve sayfalar arası geçiş yapabilmelidir.İstanbul Kodluyor sayfasında geri dönüş yapılamamalıdır. 

![Alt text](images/menubarselenium.png) 

## Test Case 2: TOBETO logosuna tıklama test edilecektir.
#### Ön Koşul : Kullanıcı platformada "https://tobeto.com/platform" sayfası dışındaki bir sayfada olamlıdır.
#### Adımlar:
#### 1. Ekranı sol üstünde bulunan TOBETO logusuna tıklayın.
#### Beklenen Sonuç: Ana sayfadan farklı bir sayfadaysa eğer kullanıcı TOBETO logosuna tıkladığında ana sayfaya yönlendirilmelidir.

![Alt text](images/tobetologo.png)

## Test Case 3: Kullanıcının isminin yazdığı butonun kontrolü Profil Bilgileri ve Oturumu Kapat durumları test edilecektir. 
#### Ön Koşul: Kullanıcı tobeto.com sayfasına giriş yapmış olmalı.
#### Adımlar:
#### 1. Ekranın sağ kısmında bulunan T logosunun yanındaki isim soyisim yazılan alana tıklayın.
#### 2. "Profil Bilgileri" yazısına tıklayın.
#### Beklenen Sonuç: Kullanıcı "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim" sayfasına erişmelidir.
#### 3. Sağ üstte bulunan TOBETO yazısına tıklayın.
#### 4. Ekranın sağ kısmında bulunan T logosunun yanındaki isim soyisim yazılan alana tıklayın.
#### 5. "Oturumu Kapat" yazısına tıklayın.
#### Beklenen Sonuç : Kullanıcı "https://tobeto.com/giris" sayfasına erişmelidir.
#### Beklenen Sonuç: Ad ve soyad bilgisinin yanında aşağı yönü gösteren bir ok bulunmalı. Kullanıcı bu alana tıkladığında açılır pencere şeklinde profil bilgileri ve oturumu kapat butonları yer almalıdır.Profil Bilgileri ve Oturum Kapat butonları tıklanmalı ve ilgili sayfaya yönlendirilmeli. 

