print("Uydurukça sözlük üretme makinesine hoş geldiniz.\nTüm kelimeleri ürettikten sonra 0'a basarak sözlüğü başlatabilirsiniz.")
TrUy={}
UyTr={}
while True:
    kelime_tr=input("Türkçe bir kelime giriniz: ")
    if kelime_tr=="0":
        print("sözlük oluşturuluyor")
        break
    else:
        kelime_uydur=input("Uydurduğunuz karşılığını giriniz: ")
        TrUy[kelime_tr]=kelime_uydur
        UyTr[kelime_uydur]=kelime_tr
        
print("sözlüğünüz şu şekildedir: ",TrUy)

while True:
    dil=input("Türkçe bir kelimenin karşılığını öğrenmek için türkçe yazınız. \nUydurukça bir kelimenin karşılığını öğrenmek için uydurukça yazınız: ")
    if dil=="türkçe":
        kelime=input("karşılığını öğrenmek istediğiniz türkçe kelimeyi giriniz: ")
        print("Uydurduğunuz karşılığı: ", TrUy.get(kelime,"geçersiz bir kelime girdiniz."))
    elif dil=="uydurukça":
        kelime=input("karşılığını öğrenmek istediğiniz uydurukça kelimeyi giriniz: ")
        print("Türkçe karşılığı: ", UyTr.get(kelime,"geçersiz bir kelime girdiniz."))
    else:
        print("galiba geçersiz bir kelime girdin")
