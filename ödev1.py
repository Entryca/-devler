Kullanici = input("Lütfen istenilen bilgileri, gösterilen formatta yazınız:Ad-Soyad,Yaş,Boy(cm),Kilo(kg),Cinsiyet(K/E):")
Kullanici = list(Kullanici.split(","))
Kullanici_ad = Kullanici[0]
Kullanici_yaş = Kullanici[1]
Kullanici_boy = float(Kullanici[2])
Kullanici_kilo = float(Kullanici[3])
Kullanici_Cinsiyet = str(Kullanici[4])

endeks = Kullanici_kilo /((Kullanici_boy/100)**2)


if Kullanici_Cinsiyet == 'E':
    print(f"Merhaba {Kullanici_ad},Siz {Kullanici_yaş} yaşında,{Kullanici_boy} cm boyunda ve {Kullanici_kilo} kg ağırlığında olduğunuz için vücut kitle yağ endeksi {float(endeks)} olan bir Erkeksiniz.")
else: 
    print(f"Merhaba {Kullanici_ad},Siz {Kullanici_yaş} yaşında,{Kullanici_boy} cm boyunda ve {Kullanici_kilo} kg ağırlığında olduğunuz için vücut kitle yağ endeksi {float(endeks)} olan bir Kadınsınız.")
