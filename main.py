"""
Veri Tipleri 1.Soru

str --> Metinsel veya karakter ifadeleri
int --> Tam Sayı
Float --> Ondalıklı Sayı
Bool --> Mantıksal İfadeler
list --> String veri tipindeki her bir karakter bir grubun yani string karakter dizisinin bir elemanıdır ve her bir elemana indeks numarası ile ulaşabiliriz.
tuple -->list' e benzer ancak farkı tuple içindeki elemanlar değiştirilemez yani tuple listesine ekleme, silme ve güncelleme yapamayız.
sets -->list' e benzer ancak fark olarak set içindeki elemanlar sıralanamaz (sort) ve indekslenemez yani set elemanlarına 0,1 şeklinde indeks numaraları ile ulaşamayız. Dolayısıyla set 'e eklediğimiz bir elemanın set listesi içinde hangi sırada olacağını bilemeyiz. Ayrıca set içerisindeki elemanlar tekrarlayamaz, her bir elemandan sadece bir tane olmalıdır, tekrarlayanlar silinir.
range --> range() fonksiyonu belirli aralıkta bulunan sayıları göstermek için kullanılır.
dict  -->Python collection veri tiplerinden olan dictionary yani sözlük veri yapısı key ve value şeklinde verileri saklayabileceğimiz bir veri yapısıdır. 
Binary: Bytes ve bytearray, ikili verileri işlemek için kullanılır. Memoryview, bir kopya oluşturmaya gerek kalmadan diğer ikili nesnelerin belleğine erişmek için arabellek protokolünü kullanır.


"""
"""
2.Soru

Mail Adresi , Şifre , Kurs İsimleri , Kurs Açıklaması  --> String

Yorum Sayıları , Gün , Tarihler --> İnt

"""

mail = "xxxx@outlook.com"
password = "12345"

eMail = input("Mail adresinizi giriniz: ")
pw = input("Password giriniz: ")


if (eMail == "xxxx@outlook.com") and (pw == "12345"):
    print("Login successful")
else:
    print("Incorrect Login Try Again")

