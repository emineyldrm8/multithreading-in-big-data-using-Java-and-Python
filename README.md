# multithreading-in-big-data-using-Java-and-Python
multithreading in big data using Java and Python

# PROJENİN AMACI
Bu porjede mus¸teri s¸ikayetleri kayıtlarının tutuldu ¨ gu˘
bir veri seti ic¸erisindeki benzer kayıtlar tespit edilecek ve
tespit edilen kayıtlar masaust ¨ u uygulamasında g ¨ osterilecektir. ¨
Multithreading kullanarak benzerlik arama suresini d ¨ us¸¨ urmek ¨
amac¸lanmaktadır.
1. Veri seti ic¸erisindeki arama is¸lem suresini multithreading ¨
kullanılarak azaltmak.
2. Belirtilen sutun/s ¨ utunlar ic¸in her bir satırdaki kayıtların ¨
birbiriyle kelime bazlı kars¸ılas¸tırılması ve aralarındaki
benzerligin tespit edilmesi. ˘
3. Uygulama ic¸erisinde istenen ozelliklere g ¨ ore kayıtları ¨
filtrelemek ve kullanıcıya gostermek. ¨
4. Masaust ¨ u uygulama gelis¸tirme hakkında bilgi ve beceriye ¨
sahip olmak.

# GİRİŞ

Projede verilen kapsamlı veri setinin duzenlenerek ¨ ust ¨ unde ¨
is¸lemler yapılması istenmektedir.Bu veri seti ilk bas¸ta
1.8 milyon veriye sahiptir.Bu veri seti ic¸erisinde Null
degerler barındırmayacak, noktalama is¸aretleri ve stop ˘
wordler silinecek, 6 sutuna sahip bir s¸ekilde tekrardan ¨
duzenlenmelidir. Yeni d ¨ uzenlenen veri seti ¨ uzerinde benzerlik ¨
is¸lemleri yapılması gerekir.Bu benzerlik kars¸ılas¸tırması sutun ¨
ic¸erisinde yapılacaktır.
˙Is¸lemlerin gerc¸ekles¸tirilmesi ic¸in bir arayuz¨
hazırlanmalıdır.Kullanıcı bu arayuz ic¸erisinde benzerlik ¨
oranını, bu benzerlik oranının is¸lenecegi s ˘ utunu, kac¸ thread ¨
ile bu is¸lemi gerc¸ekles¸tirecegini sec¸ecektir.Daha sonra ˘
yapılan sec¸imlerin sonucu arayuz¨ uzerinde bir tabloda ¨
gosterilecektir.Bu is¸lemlerin s ¨ uresi de aynı s¸ekilde aray ¨ uzde ¨
gosterilmelidir. ¨
Biz projemizde Java programlama dilini kullanarak hem
thread yapısını hem de Swing framework’u ile dinamik bir ¨
ara yuz olus¸turduk.

# YÖNTEM

˙Ilk olarak projemizde kullanacagımız veri setini indirdik.Bu ˘
veri seti ilk bas¸ta 1.8 milyon veriye sahipti.Bu veriler
ic¸erisinde null degerler,noktalama is¸aretleri ve stop wordler ˘
bulunmaktaydı.Biz bu veri setini duzenledik. ¨
˙Ic¸erisindeki
null degerleri,noktalama is¸aretlerini ve stop wordleri ˘
sildik.Daha sonra verileri ”Product(Ur ¨ un), Issue (Konu), ¨
Company(S¸irket), State, Complaint ID, Zip Code” adlarında
6 adet sutuna ayırdık.En son haliyle veri setimiz toplamda ¨
1.2 milyon kayıt ic¸ermektedir.Bu veri setini ise bir csv
dosyasında tuttuk.(Kodlarda ”Yazlab2.csv” adlı dosyaya denk
gelmektedir.)
Daha sonra Kullanıcının is¸lemler gerc¸ekles¸tirecegi aray ˘ uz¨ u¨
yaptık.Arayuz¨ um¨ uz¨ u java Swing framework’ ¨ un¨ u kullanarak ¨
gerc¸ekles¸tirdik.Arayuz¨ um¨ uzde kullanıcı tarafından benzerlik ¨
oranının girilebilecegi,hangi s ˘ utunların sec¸ilebilece ¨ gi,thread ˘
sayılarının girilebilecegi bir b ˘ ol¨ um yer almakta.Ayrıca ¨
threadlerin c¸alıs¸ma surelerini de hesaplayan ve bu hesabı ¨
kullanıcıya gosteren bir kısım yer almakta.Kullanıcının ¨
yaptıgı is¸lemleri sonucunda c¸ıkan sonuc¸lar aray ˘ uzde bir tablo ¨
ic¸erisinde kullanıcıya gosterilmektedir.Bu da dinamik bir ¨
arayuz¨ u¨ ozelli ¨ gi sa ˘ glamaktadır. ˘
Arayuz¨ um¨ uz aslında 4 tanedir. ¨
˙Ilk olarak kod c¸alıs¸tırıldıgında ˘
kars¸ımıza c¸ıkan giris¸ sayfasıdır.Bu sayfada hangi senaryonun
gerc¸ekles¸tirilecegi sec¸ilecektir.(Kodlarda ”mainPage.java” ˘
olarak gec¸mektedir)Daha sonra kullanıcının sec¸tigi is¸leme ˘
gore kars¸ısına 3 farkı ekran c¸ıkar. ¨
˙Ilk olarak aynı ur¨ unler ic¸in filtreleme is¸lemini sec¸en ¨
kullanıcı kars¸ısına c¸ıkan ekranda %100 benzerlik kayıtlarını
gor¨ unt ¨ ulemek istedi ¨ gi s ˘ utunları ve bu s ¨ utunları hangi de ¨ gerlere ˘
gore listeleyece ¨ gini sec¸ebilir. ˘
˙Ikinci sayfada ise kullanıcı ust ¨ unde is¸lem yapaca ¨ gı s ˘ utunu ¨
sec¸ebilir.Bu sutunda g ¨ ormek istedi ¨ gi benzerlik oranını ve ˘
gelen verilerin hangi sıraya gore listelenece ¨ gini ayarlayabilir. ˘
Uc¸ ¨ unc ¨ u sayfada ise kullanıcı yine aynı s¸ekilde is¸lem yapaca ¨ gı˘
sutunu sec¸ip benzerlik oranlarını ayarlayabilir.Kullanıcı icin
olus¸turdugumuz aray ˘ uz¨ un is¸leyis¸i bu s¸ekildedir. ¨
Projede multithreading kullanmamız gerektigi ic¸in ilk ˘ once ¨
bu konu uzerinde aras¸tırmalarımızı gerc¸ekles¸tirdik.Nasıl ¨
kullanmamız gerektigini ˘ o¨grendik. ˘
˙Is¸lemleri Java
kullanarak gerc¸ekles¸tirdik.Multithread yapısını ise is¸imizi
kolaylas¸tırması ac¸ısından thread pool yapısını kullanarak
gerc¸ekles¸tirdik.Thread pool yapısı ic¸erisinde 5 adet thread
kullandık.Bu threadlerin is¸leyis¸ zamanını hesaplayabilmek
ic¸in ise thread pool ic¸erisinde is¸lemin bas¸langıc¸ ve bitis¸
zamanlarını yazdırıp gec¸en sureyi hesapladık. ¨
Arayuz¨ um¨ uzden ve projenin genelinden g ¨ or¨ unt ¨ uleri as¸a ¨ gıda ˘
gorebilirsiniz.

# SCREENSHOTS

![image](https://user-images.githubusercontent.com/73225797/221418501-ed297480-97d5-416e-89d7-f624fd88ac01.png)

![image](https://user-images.githubusercontent.com/73225797/221418518-5a7b6d0a-f9f5-4384-8286-0134c91ecc6a.png)

<br></br>
DOSYANIN GÖRÜNTÜSÜ
<br></br>
![image](https://user-images.githubusercontent.com/73225797/221418564-3cf41cdc-9069-457e-b3ad-3cb9adc7238a.png)

# AKIŞ DİYAGRAMI
![image](https://user-images.githubusercontent.com/73225797/221418587-0fe31d7a-692f-425b-94f8-03818f2ca5e4.png)

