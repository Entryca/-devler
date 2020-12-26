Ogrenci = "Murat can Yalçınkaya"
import sys


def welcome ():             #Oturuma Giriş;
    Hak =3
    while Hak >0:
        girilen_ad = input("Adınızı Soyadınızı Giriniz:  ")
        if girilen_ad == Ogrenci :
            return print ("Hoşgeldiniz " + girilen_ad )
        else :
            Hak -= 1
            print("Giriş Bilgileriniz Yanlış.Lütfen tekrar deneyin.")
    sys.exit("Lütfen sonra tekrar deneyin.")

welcome()   #----

Dersler = []              #Derslere Giriş;

Dersler = input("Aldığınız Derslerin Aralarına virgül(,) koyarak yazınız: ")
Dersler = list(Dersler.split(","))

def Ders_secim():
    if len(Dersler) > 5 :
        print(Ogrenci + " 5'ten fazla ders alamazsınız.")
    elif len(Dersler) < 3 : 
        print(Ogrenci + " Başarısız Oldun.")
    else :
        print(" Aldığınız Dersler " + str(Dersler)) 

Ders_secim()

import random          #Değişiklik olsun dersi kullanıcının seçtiği dersler arasından rastgele seçelim.
Ders = random.choice(Dersler)

def Sınavlar():
    Derece = input ((Ders) + " dersinden aldığınız notları vize,final,proje formatında giriniz: ")
    Derece = list(Derece.split(","))
    
    vize = float(Derece[0])
    final = float(Derece[1])
    proje = float(Derece[2])
    Sonuc = vize*.3 + final*.5 + proje*.2

    if Sonuc > 90 :
        print("Tebrikler " + str(Ders) + " Dersinden " + str(Sonuc) + " ile AA aldın.")
    elif Sonuc > 70 :
        print("Tebrikler " + str(Ders) + " Dersinden " + str(Sonuc) + " ile BB aldın.")
    elif Sonuc > 50 :
        print("Tebrikler " + str(Ders) + " Dersinden " + str(Sonuc) + " ile CC aldın.")
    elif Sonuc > 30 :
        print("Tebrikler " + str(Ders) + " Dersinden " + str(Sonuc) + " ile DD aldın.")
    else :
        print("Tekrar Görüşmek Üzere " + str(Ders) + " Dersinden " +str(Sonuc) + " ile FF Çaktın.")

Sınavlar()
