print("kliniğimize hoş geldiniz:)")
print("\nSIRA ALMAK İÇİN İSMİNİZİ GİRİNİZ.")
print("\nSIRADAKİ HASTAYI GÖRMEK İÇİN sıradaki YAZINIZ")
print("\nGÜN SONUNDA bitti YAZARAK ERTESİ GÜNE KALAN HASTALARI GÖREBİLİRSİNİZ.\n")
hastalar=[]
while True:
    ad=input("adınızı giriniz:")
    if ad in hastalar:
        i=hastalar.index(ad)
        print("sıranız: ",i+1)
    elif ad=="sıradaki":
        if len(hastalar)==0:
            print("sırada hasta yok")
        else:
            print(hastalar.pop(0))
    elif ad=="bitti":
        break
    elif ad not in hastalar:
        hastalar.append(ad)
        print("sıra alındı. sıranız: ",(hastalar.index(ad))+1)
        
sira=hastalar.count("sıradaki")
for i in range(sira):
    hastalar.pop()
print("kalan kişiler: ", hastalar)
