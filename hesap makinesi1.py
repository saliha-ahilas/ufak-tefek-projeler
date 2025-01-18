print("hesap makineme hoş geldiniz<3, oturun lütfen")
print("aşağıda işlemlere karşılık gelen kodlar belirtilmiştir")
print("toplama=1")
print("çıkarma=2")
print("çarpma=3")
print("bölme=4")
print("üssünü alma=5")
print("çıkmak için 0'a basınız")
while True:
    islem=input("yapmak istediğiniz işlemi seçiniz(çıkmak için 0'a basınız): ")
    if islem in ["1","2","3","4","5"]:
        try:
            if islem in ["1","2","3","4"]:
                    a=float(input("birinci sayıyı giriniz: "))
                    b=float(input("ikinci sayıyı giriniz: "))
                    if (islem == "1"):
                        print(f"{a}+{b}={a+b}")
                    elif (islem == "2"):
                        print(f"{a}-{b}={a-b}")
                    elif (islem == "3"):
                        print(f"{a}*{b}={a*b}")
                    elif (islem == "4"):
                        if b==0:
                            print("bir sayının sıfır bölümü tanımsızdır.")
                        else:
                            print(f"{a}/{b}={a/b}")
            elif (islem =="5"):
                c=float(input("tabandaki sayıyı yazınız: "))
                d=float(input("üsteki sayıyı yazınız: "))
                print(f"{c}üssü{d}={c**d}")
        except ValueError:
            print("lütfen geçerli bir sayı giriniz")
    elif islem not in ["0","1","2","3","4","5"]:
        print("lütfen geçerli bir işlem kodu giriniz")
    elif islem == "0":
        break
