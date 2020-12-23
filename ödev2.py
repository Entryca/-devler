Birey = input("Lütfen İstenilen Bilgileri Gösterilen Formatta Sırasıyla Giriniz:Ad Soyad,Yaş,Doğum Yılı:")

Birey= list(Birey.split(","))
Birey_ad = Birey[0]


for i in Birey:
    print(i)

if int(Birey[1]) < 18:
    print(f"{Birey_ad} dışarı çıkamazsınız.Çünkü çok tehlikeli.")
else:
    print(f"{Birey_ad} dışarı çıkabilirsiniz.")