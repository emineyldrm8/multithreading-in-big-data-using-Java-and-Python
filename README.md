# multithreading-in-big-data-using-Java-and-Python
multithreading in big data using Java and Python

# PROJENİN AMACI
Bu projede müşteri şikayetleri kayıtlarının tutulduğu
bir veri seti içerisindeki benzer kayıtlar tespit edilecek ve
tespit edilen kayıtlar masaüstü uygulamasında gösterilecektir.
Multithreading kullanarak benzerlik arama suresini düşürmek
amaçlanmaktadır.
1. Veri seti içerisindeki arama işlem süresini multithreading 
kullanılarak azaltmak.
2. Belirtilen sütun/sütunlar için her bir satırdaki kayıtların 
birbiriyle kelime bazlı karşılaştırılması ve aralarındaki
benzerliğin tespit edilmesi. 
3. Uygulama içerisinde istenen özelliklere göre kayıtları
filtrelemek ve kullanıcıya gostermek. 
4. Masaüstü uygulama geliştirme hakkında bilgi ve beceriye 
sahip olmak.

# GİRİŞ

Projede verilen kapsamlı veri setinin düzenlenerek üstünde
işlemler yapılması istenmektedir.Bu veri seti ilk başta
1.8 milyon veriye sahiptir.Bu veri seti içerisinde Null
değerler barındırmayacak, noktalama işaaretleri ve stop 
wordler silinecek, 6 sütuna sahip bir şekilde tekrardan 
düzenlenmelidir. Yeni düzenlenen veri seti üzerinde benzerlik 
işlemleri yapılması gerekir.Bu benzerlik karşılaştırması sütun içerisinde yapılacaktır.
İşlemlerin gerçekleştirilmesi için bir arayüz
hazırlanmalıdır.Kullanıcı bu arayuz içerisinde benzerlik 
oranını, bu benzerlik oranının işlenecegi sütunu, kaç thread 
ile bu işlemi gerçekleştirecegini seçecektir.Daha sonra 
yapılan seçimlerin sonucu arayüz üzerinde bir tabloda 
gösterilecektir.Bu işlemlerin süresi de aynı şekilde arayüzde 
gösterilmelidir. 
Projemde Java programlama dilini kullanarak hem
thread yapısını hem de Swing framework’u ile dinamik bir 
arayüz oluşturdum.



# SCREENSHOTS

![image](https://user-images.githubusercontent.com/73225797/221418501-ed297480-97d5-416e-89d7-f624fd88ac01.png)

![image](https://user-images.githubusercontent.com/73225797/221418518-5a7b6d0a-f9f5-4384-8286-0134c91ecc6a.png)

<br></br>
DOSYANIN GÖRÜNTÜSÜ
<br></br>
![image](https://user-images.githubusercontent.com/73225797/221418564-3cf41cdc-9069-457e-b3ad-3cb9adc7238a.png)

# AKIŞ DİYAGRAMI
![image](https://user-images.githubusercontent.com/73225797/221418587-0fe31d7a-692f-425b-94f8-03818f2ca5e4.png)

