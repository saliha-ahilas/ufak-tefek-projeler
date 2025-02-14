print("zikirmatik uygulamasına hoş geldiniz")
devammi="d"
geneltoplam=0
zikirler=[]
while devammi!="ç":
    devammi="d"
    a=0
    try:
        b=input("hangi zikri çekmek istiyorsunuz: ").capitalize()
        zikirler.append(b)
        c=int(input("bu zikri kaç kere çekmek istiyorsunuz: "))
        print("her zikir çektiğinizde enter tuşuna basabilirsiniz")
        while devammi=="d":
            for i in range(c):
                a+=1
                geneltoplam+=1
                input(f"{b} zikrini {a} kez çektiniz.")
            devammi=input(f"{c} oldu devam etmek için d'ye, çıkmak için ç'ye, başka zikre geçmek için z'ye tıklayınız:").lower()
            if devammi=="ç" or devammi=="z":
                break
    except ValueError:
        print("Geçerli bi değer giriniz")
    print(f"toplam {a} tane {b} zikri çektiniz")
print(f"bugün toplam {geneltoplam} tane {zikirler} zikri çektiniz")
    
            
