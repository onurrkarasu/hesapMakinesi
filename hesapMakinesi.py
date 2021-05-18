secenek="""
        [1] Toplama - [2] Çıkarma - [3] Çarpma - [4] Bölme -  [5] Üs alma
         """

print(secenek)
secenek=int(input("Seçiminizi Yapın : "))
sayilar=input("İşlem yapılacak sayıları aralarında birer boşluk bırakarak girin : ")
sayilar_bolunmus=sayilar.split(" ")

if secenek==1:
    ilk_sayi=float(sayilar_bolunmus[0])
    ikinci_sayi = float(sayilar_bolunmus[1])
    toplama=ilk_sayi+ikinci_sayi
    print(" = Toplama İşleminin Sonucu  : "+str(toplama))
elif secenek==2:
    ilk_sayi = float(sayilar_bolunmus[0])
    ikinci_sayi = float(sayilar_bolunmus[1])
    cikar = ilk_sayi - ikinci_sayi
    print("Çıkarma İşleminin Sonucu  : " + str(cikar))
elif secenek==3:
    ilk_sayi = float(sayilar_bolunmus[0])
    ikinci_sayi = float(sayilar_bolunmus[1])
    carpma = ilk_sayi * ikinci_sayi
    print("Çarpma İşleminin Sonucu  : " + str(carpma))
elif secenek==4:
    ilk_sayi = float(sayilar_bolunmus[0])
    ikinci_sayi = float(sayilar_bolunmus[1])
    bol = ilk_sayi / ikinci_sayi
    print("Bölme İşleminin Sonucu " + str(bol))
elif secenek==5:
    ilk_sayi = float(sayilar_bolunmus[0])
    ikinci_sayi = int(sayilar_bolunmus[1])
    usAlma = ilk_sayi ** ikinci_sayi
    print("Üs Alma Sonucu  : "+str(usAlma))
else:
    print("hata")