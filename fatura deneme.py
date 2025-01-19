print("Kırtasiyemize hoş geldininiz:)")
print("\nTÜM ÜRÜNLERİ GİRDİKTEN SONRA TOPLAM ALIŞVERİŞ TUTARI İÇİN ÜRÜN İSMİ YERİNE 0 YAZINIZ.")
ad=input("\nLütfen adınızı giriniz: ")
toplamtutar=0
liste=[]
urunsırası=1
while True:
    try:
        print("\n", urunsırası,". ürün")
        urun=input("ürün ismi giriniz: ")
        if (urun=="0"):
            break
        else:
            adet=int(input("ürün adedini giriniz: "))
            fiyat=float(input("ürün fiyatını giriniz: "))
            tutar=adet*fiyat
            toplamtutar += tutar
            liste.append(urun)
            urunsırası+=1

    except ValueError:
        print("lütfen geçerli bir sayı giriniz.")
    
print("Sayın; ",ad)
print("aldığınız ürünler; ",liste)
print("Alışveriş tutarınız",toplamtutar,"tl'dir")
print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.")
